__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

import os
from pathlib import Path

class NKMergeUserCode:

    def __init__(self, oldFile, newFile, UserCodeStartKey="USER_CODE_START", UserCodeEndKey="USER_CODE_END", keepBackup=True):
        self.oldFile =oldFile
        self.newFile = newFile
        self.UserCodeStartKey = UserCodeStartKey
        self.UserCodeEndKey =UserCodeEndKey
        self.result= ""
        self.keepBackup=keepBackup

        
    def isSameUserCodeGuard(self, g1 , g2):
        g11=g1
        g22=g2
        
        #preprocess strings before comaprision, just in case the user changes something
        for x in range(3):
            g11=g11.replace("  ", " ");
            g22=g22.replace("  ", " ");
            g11=g11.replace(" \t", " ");
            g22=g22.replace(" \t", " ");

        return (g11==g22)         
            
        
    def merge(self):
    
        #
        newFile = self.newFile
        oldFile = self.oldFile
        UserCodeStartKey=self.UserCodeStartKey
        UserCodeEndKey=self.UserCodeEndKey
        curretUserCode=""
        numSectionsMerger=0
        
        #check if we have the files first
        if not os.path.exists(newFile):
            print (f'the file {newFile} cannot be found\n')
            return False
        
        
        if not os.path.exists(oldFile):
            print (f'the file {oldFile} cannot be found\n')
            return False
        
        
        #read data from the old file
        oldFileHandler = open(oldFile, 'r')
        oldFileLines = oldFileHandler.readlines()
        oldFileHandler.close()
        
        #read data from the new file
        newFileHandler = open(newFile, 'r')
        newFileLines = newFileHandler.readlines()
        newFileHandler.close()
        
        #create a new file where we will merge all
        inOldUserCode=False
        inNewUserCode=False
        mergeFileLines=[]
        for newLine in newFileLines:
            if (inOldUserCode): 
                print (f"Error in {curretUserCode}")
            if UserCodeStartKey in newLine: #we found a user code in the new file.
                mergeFileLines.append(newLine)
                curretUserCode = newLine
                inNewUserCode = True
                for oldLine in oldFileLines: 
                    if self.isSameUserCodeGuard(newLine , oldLine): #we found the same user code in the old file
                        inOldUserCode = True
                    elif  UserCodeEndKey in  oldLine and inOldUserCode :
                        inOldUserCode = False
                        break
                    elif inOldUserCode:    
                        mergeFileLines.append(oldLine)
                        numSectionsMerger+=1

            elif UserCodeEndKey in newLine:
                inNewUserCode=False
                mergeFileLines.append(newLine)
            elif not inNewUserCode: 
                mergeFileLines.append(newLine)
            
        if (inOldUserCode):
            print(f'Error merging see: {inUserCode}')
            return False
            
        if (numSectionsMerger==0):
            return True
            
        #merging is probably ok now
        #rename the new file
        
        p = Path(newFile)
        backupFile = p.with_suffix('.back')
        if os.path.exists(backupFile):
            os.remove(backupFile)
        os.rename(newFile, backupFile)   

        #write the merge data to the new file
        st="" 
        for Line in mergeFileLines:
            st+=Line
            
        out = open(newFile, "w")
 
        #write string to file
        out.write(st)
 
        #close file
        out.close()  
        
        #remove backup if not needed
        if not self.keepBackup:
            os.remove(backupFile)
        
        return True
        
    def __str__(self):

        st = {self.result}
        return st
        
        
if __name__ == "__main__":
#test code

    oldFile_="old.txt"
    newFile_="new.c"
    UserCodeStartKey_="USER_CODE_START"
    UserCodeStartKey_="USER_CODE_END"
    
    merger = NKMergeUserCode(oldFile=oldFile_, newFile=newFile_, UserCodeStartKey=UserCodeStartKey_, UserCodeEndKey=UserCodeStartKey_, keepBackup=True)
    
    if merger.merge():
        print ("merge OK \n")
    else :
        print ("merge NOK \n")
        