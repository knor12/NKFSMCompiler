__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from NKModelRoot import *
from NKModelTransition import *
#from NKConfigToTransitions import *
from NKGeneratorGlueHeader import *
from NKGeneratorGlueSource import *
from NKGeneratorFSMHeader import *
from NKGeneratorFSMSource import *
from NKMergeUserCode import *
from Beautifier import *
import sys
import os
from pathlib import Path



if __name__ == "__main__":


    beautifier = Beautifier() 

    #process command line arguments for input configuration file
    file =  sys.argv[1]
    UserCodeStartKey_="USER_CODE_START"
    UserCodeEndKey_="USER_CODE_END"
    
    #check if file exists
    if not os.path.exists(file):
        print (f'Configuration file {file} not found')
        exit()
    
    
    path = file 
    
    #find the extension of the configuration file
    filename, file_extension = os.path.splitext(path)
    #print(f"file name={filename}, file extension={file_extension}")
    reader = 0
    if ".csv" == file_extension:
        reader = NKConfigToTransitions()
    elif ".scxml" == file_extension:
        reader = NKRootModel()
    else:
        print(f"extension of {path} not identified\n")
        exit( False)
        
    
    #read configuration
    if not reader.read(ConfigPath =path):
        exit()
        
    print("Configuration read OK")    
           
    #print configuration model read
    model = reader
    #print (model)  
    
    

    #build the glue header
    glueHeaderWriter = NKGeneratorGlueHeader(transitions=model, directory="./")
    st = f'glueHeader{glueHeaderWriter}' 
    print(st)
    #if file exists rename it
    fileName= glueHeaderWriter.getFileName()
    if os.path.exists(fileName):
        p = Path(fileName)
        oldFile_ = p.with_suffix('.hold')
        if os.path.exists(oldFile_):
            os.remove(oldFile_)
        os.rename(fileName, oldFile_)
        glueHeaderWriter.writeToFile()
        print(f'{fileName} generated OK') 
        merger = NKMergeUserCode(oldFile=oldFile_, newFile=fileName, UserCodeStartKey=UserCodeStartKey_,UserCodeEndKey=UserCodeEndKey_ , keepBackup=False)
        if merger.merge():
            beautifier.beatify(fileName)
            print (f"{fileName} and {oldFile_} merge OK \n")
        else :
            print (f"{fileName} and {oldFile_} merge NOK \n")
            exit()
        
    else: 
        beautifier.beatify(fileName)
        glueHeaderWriter.writeToFile()
        print(f'{fileName} generated OK')    
        
     

    #build the glue source
    glueSourceWriter = NKGeneratorGlueSource(transitions=model, directory="./")
    st = f'{glueSourceWriter}' 
        #if file exists rename it
    fileName= glueSourceWriter.getFileName()
    if os.path.exists(fileName):
        p = Path(fileName)
        oldFile_ = p.with_suffix('.cold')
        if os.path.exists(oldFile_):
            os.remove(oldFile_)
        os.rename(fileName, oldFile_)
        glueSourceWriter.writeToFile()
        print(f'{fileName} generated OK')
        merger2 = NKMergeUserCode(oldFile=oldFile_, newFile=fileName,UserCodeStartKey=UserCodeStartKey_,UserCodeEndKey=UserCodeEndKey_, keepBackup=False)
        if merger2.merge():
            beautifier.beatify(fileName)
            print (f"{fileName} and {oldFile_} merge OK \n")
        else :
            print (f"{fileName} and {oldFile_} merge NOK \n")
        
    else: 
        glueSourceWriter.writeToFile()
        beautifier.beatify(fileName)
        print(f'{fileName} generated OK')    

    #build the fsm header
    FSMHeaderWriter = NKGeneratorFSMHeader(transitions=model, directory="./")
    #st = f'{FSMHeaderWriter}' 
    #print(st)
    FSMHeaderWriter.writeToFile()
    beautifier.beatify(f'{FSMHeaderWriter.filename}.h')
    print(f'{FSMHeaderWriter.filename}.h generated OK')     
    
    #build the FSM source
    FSMSourceWriter = NKGeneratorFSMSource(transitions=model, directory="./")
    #st = f'{FSMSourceWriter}' 
    #print(st)
    FSMSourceWriter.writeToFile()
    beautifier.beatify(f'{FSMHeaderWriter.filename}.c')
    print(f'{FSMHeaderWriter.filename}.c generated OK')    