__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from NKTransitions import *
from NKTransition import *
from NKConfigToTransitions import *
from datetime import date
import os 

class NKGeneratorFSMSource:

    def __init__(self, transitions, directory):
        self.transitions =transitions
        self.directory=directory
        self.filename=f'{transitions.Name}FSM'
        self.GlueName=f'{transitions.Name}Glue'
        self.FSMStates_t=f'FSM{transitions.Name}_State_t'
        self.structName = f'{transitions.Name}FSM'
   
    def __str__(self):
        events = self.transitions.getEvents()
        states = self.transitions.getStates()
        transitions = self.transitions.transitions
        
        
        st = f"\
/*\n\
*this file is auto generated by NKCompiler, do not edit manualy \n\
*@file {self.filename}.c\n\
*@date {date.today()}\n\
*@author n.kessa\n\
*@brief state machine {self.filename} FSM code\n\
*/\n\
\n\
#include \"{self.filename}.h\" \n\
#include \"{self.GlueName}.h\" \n\
\n\
#include <stdlib.h> \n\
\n\
\n\
#define MAX_NUM_STATES ({len(states)})\
\n\
\n\
"

#add the initialization function
        st+=f"\n\
/*initialization function*/\n\
void {self.structName}_Init(struct {self.structName} * fsm)\n\
{{\n\
    fsm->state={self.transitions.initialState};\n\
}}"

#add routing for each event
        for event in events:
            #event handler name
            st+=f'\n\n\
int {self.structName}_{event}(struct {self.structName} * fsm, void * o)\n\
{{\n\
\n\
    int ret = 0; \n'
            for transition in transitions:
                if event == transition.Event:
                    st+=f"\
    if ((fsm->state == {transition.OriginalState}){transition.Condition})\n\
    {{\n\
        ret = {transition.TransitionHandler}(o);\n\
        if (ret >= 0)\n\
        {{\n\
            fsm->state = {transition.NewState};\n\
        }}else \n\
        {{\n\
            fsm->state = {self.transitions.errorSate};\n\
        }}\n\
        return ret;\n\
    }}\n\
    \n"

            st+=f'\
    return 0;\n\
}}\n'


        return st
        
        
    def writeToFile(self):
        filename = self.filename
        filePath=os.path.join(self.directory,filename+".c" )
        #it is OK to overide FSM source, the user should edit it manualy any ways
        #while (os.path.exists(filePath)):
        #   filename = filename + "New" 
        #   filePath=os.path.join(self.directory,filename+".c" ) 
        
        print(f'writing to {filePath}')    
        out = open(filePath, "w")
 
        #write string to file
        out.write(f'{self}')
 
        #close file
        out.close()   