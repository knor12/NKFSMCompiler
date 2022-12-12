__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from NKModelRoot import *
from NKModelTransition import *
#from NKConfigToTransitions import *
from datetime import date
import os 

class NKGeneratorGlueSource:

    def __init__(self, transitions, directory):
        self.transitions =transitions
        self.directory=directory
        self.filename=f'{transitions.Name}Glue'
        self.UserCodeStartKey = "USER_CODE_START"
        self.UserCodeEndKey ="USER_CODE_END"
        self.userCodeImports=f'\n/*{self.UserCodeStartKey}_IMPORTS*/\n\n\n/*{self.UserCodeEndKey}_IMPORTS*/\n\n'
   
    def getFileName(self):
        filename = self.filename
        filePath=os.path.join(self.directory,filename+".c" )
        return filePath; 
    
    def __str__(self):
        handlers = self.transitions.getHandlers()
        st = f"\
/*\n\
*this file is auto generated by NKCompiler\n\
*@file {self.filename}.c\n\
*@date {date.today()}\n\
*@author n.kessa\n\
*@brief state machine {self.filename} glue code\n\
*/\n\
\n\
#include \"{self.filename}.h\" \n\
{self.userCodeImports}\
\n"
        for handler in handlers:
            userCodeSection = f'\
    /*{self.UserCodeStartKey}_{handler}*/\n\
    (void)o;\n\
    printf("in handler:%s\\n", __FUNCTION__ );\n\
    return 0;\n\
    /*{self.UserCodeEndKey}_{handler}*/\n'
    
            st+=f"\n\
int {handler}(void * o)\n\
{{\n\
/*add your glue code below*/\n\
{userCodeSection}\
\n\
}}"
#\n\
#{\n\
#    
#    return 0;\n\
#}\n\n"
        return st
        
        
    def writeToFile(self):
        filename = self.filename
        filePath=os.path.join(self.directory,filename+".c" )
        #while (os.path.exists(filePath)):
        #   filename = filename + "New" 
        #   filePath=os.path.join(self.directory,filename+".c" ) 
        
        print(f'writing to {filePath}')    
        out = open(filePath, "w")
 
        #write string to file
        out.write(f'{self}')
 
        #close file
        out.close()   