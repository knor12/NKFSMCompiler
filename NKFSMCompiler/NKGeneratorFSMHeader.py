__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from NKModelRoot import *
from NKModelTransition import *
from NKFSMVersion import *
from datetime import date
import os 

class NKGeneratorFSMHeader:

    def __init__(self, transitions, directory):
        self.transitions =transitions
        self.directory=directory
        self.filename=f'{transitions.Name}FSM'
        self.guard = f'{transitions.Name}FSM_H'
        self.structName = f'{transitions.Name}FSM'
        self.FSMStates_t=f'FSM{transitions.Name}_State_t'
        self.FSMEvents_t=f'FSM{transitions.Name}_event_t'
        self.CPPGuardStart = f'\n#ifdef __cplusplus \nextern \"C\" \n{{ \n#endif		/* __cplusplus */ \n'
        self.CPPGuardEnd = f'#ifdef __cplusplus\n}}\n#endif		/* __cplusplus */\n'
    
    def __str__(self):
        Events = self.transitions.getEvents()
        states = self.transitions.getStates()
        st = f"\
/*\n\
*this file is auto generated by NKCompiler {NKFSMVersion().getVersion()}, do not edit manualy\n\
*@file {self.filename}.h\n\
*@date {date.today()}\n\
*@author n.kessa\n\
*@brief state machine {self.filename} FSM code\n\
*/\n\
\n\
\n\
#ifndef  {self.guard}\n\
#define  {self.guard}\n\
\n\
{self.CPPGuardStart}\
/*definition of all states*/\n\
typedef enum \n\
{{"
        for state_ in states: 
            st+=f'\n\
    {state_},'
        st+=f"\n\
}}{self.FSMStates_t};\n\n\
\n"
        st+=f"\n\
/*definition of all events*/\n\
typedef enum \n\
{{"
        for event_ in Events: 
            st+=f'\n\
    {event_},'       
       
        st+=f"\n\
}}{self.FSMEvents_t};\n\n\
\n"

        st+=f"\
/*definition of state structure*/\n\
struct {self.structName} \n\
{{\
\n\
   {self.FSMStates_t} state;\n\
   int transitions; \n /*incremented every time a transition happens*/\
\n\
}};"
        st+=f"\n\
/*initialization function*/\n\
void {self.structName}_Init(struct {self.structName} * fsm);\n\
\n"


        st+=f"\n\
/*events*/\n"
        for event in Events:
            st+=f"int {self.structName}_{event}(struct {self.structName} * fsm, void * o);\n"
        st+=f"\n\
{self.CPPGuardEnd}\
#endif /*{self.guard}*/"

        #return string of file content
        return st
        
        
    def writeToFile(self):
        filename = self.filename
        filePath=os.path.join(self.directory,filename+".h" )
        #it is ok to overise this file, the use ris not suppose to edit it
        #while (os.path.exists(filePath)):
        #   filename = filename + "New" 
        #   filePath=os.path.join(self.directory,filename+".h" ) 
        
        print(f'writing to {filePath}')    
        out = open(filePath, "w")
 
        #write string to file
        out.write(f'{self}')
 
        #close file
        out.close()   