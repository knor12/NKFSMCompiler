__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from NKTransitions import *
from NKTransition import *
from NKConfigToTransitions import *
from NKGeneratorGlueHeader import *
from NKGeneratorGlueSource import *
from NKGeneratorFSMHeader import *
from NKGeneratorFSMSource import *
import sys



if __name__ == "__main__":


    #process command line arguments for input configuration file
    file =  sys.argv[1]
    
    #check if file exists
    if not os.path.exists(file):
        print (f'Configuration file {file} not found')
        exit()
    
    
    path = file #"./BulbConfig.csv"
    reader = NKConfigToTransitions()
    
    #read configuration
    if not reader.read(ConfigPath =path):
        exit()
           
    #print configuration model read
    model = reader.getTransitions()
    print (model)  

    #build the glue header
    glueHeaderWriter = NKGeneratorGlueHeader(transitions=model, directory="./")
    st = f'{glueHeaderWriter}' 
    print(st)
    glueHeaderWriter.writeToFile()

    #build the glue source
    glueSourceWriter = NKGeneratorGlueSource(transitions=model, directory="./")
    st = f'{glueSourceWriter}' 
    print(st)
    glueSourceWriter.writeToFile() 

    #build the fsm header
    FSMHeaderWriter = NKGeneratorFSMHeader(transitions=model, directory="./")
    st = f'{FSMHeaderWriter}' 
    print(st)
    FSMHeaderWriter.writeToFile()    
    
    #build the FSM source
    FSMSourceWriter = NKGeneratorFSMSource(transitions=model, directory="./")
    st = f'{FSMSourceWriter}' 
    print(st)
    FSMSourceWriter.writeToFile() 