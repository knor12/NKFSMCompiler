__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

import NKModelTransition
import copy

class NKModelTransition:

    def __init__(self):
        self.OriginalState =""
        self.Event = ""
        self.NewState = "" 
        self.Condition = ""
        self.TransitionHandler = ""
        self.Comment = ""
        self.OnExit=""
        self.OnEnter=""
        self.OnExitRaiseEvent = ""
        self.OnEntryRaiseEvent = ""

    def clone(self):
        image = copy.deepcopy(self)
        return image        
        
    def __str__(self):
        s=""
        if self.OriginalState!="" and self.OriginalState!=None:
            s+= f'OriginalState={self.OriginalState}, ' 
            
        if self.Event!=""and self.Event!=None:
            s+=f'Event= {self.Event }, '
        
        if self.NewState!=""and self.NewState!=None:
            s+=f'NewState={self.NewState}, '
        
        if self.Condition!="" and self.Condition!=None:
            s+=f'Condition={self.Condition }, '
        
        if self.TransitionHandler!="" and self.TransitionHandler!=None:
            s+=f'TransitionHandler={self.TransitionHandler }, '
        
        if self.Comment!="" and self.Comment!=None:
            s+=f'Comment={self.Comment}, '
        
        if self.OnExit!=""and self.OnExit!=None:
            s+=f'OnExit={self.OnExit}, '
        
        if self.OnEnter!=""and self.OnEnter!=None:
            s+=f'OnEnter={self.OnEnter}, '
        
        if self.OnExitRaiseEvent!=""and self.OnExitRaiseEvent!=None:
            s+=f'OnExitRaiseEvent={self.OnExitRaiseEvent}, '
        
        if self.OnEntryRaiseEvent!="" and self.OnEntryRaiseEvent!="None":
            s+=f'OnEntryRaiseEvent={self.OnEntryRaiseEvent}'
            
            
        return s    