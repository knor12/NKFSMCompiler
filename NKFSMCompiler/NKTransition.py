__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

import NKTransition
import copy

class NKTransition:

    def __init__(self, OriginalState, Event, NewState , TransitionHandler,Condition, Comment):
        self.OriginalState =OriginalState
        self.Event = Event
        self.NewState = NewState 
        self.Condition = Condition
        self.TransitionHandler = TransitionHandler.replace("\n" , "")
        self.Comment = Comment.replace("\n" , "")
        self.OnExit=""
        self.OnEnter=""
        self.OnExitRaiseEvent = ""
        self.OnEntryRaiseEvent = ""
        
    def clone(self):
        #image = NKTransition(OriginalState="", Event="", NewState="" , TransitionHandler="",Condition="", Comment="")
        #self.OriginalState=self.OriginalState
        #self.Event=self.Event
        #self.NewState=self.NewState
        #self.Condition =self.Condition 
        #self.TransitionHandle=self.TransitionHandler
        #self.Comment=self.Comment
        #self.OnExit=self.OnExit
        #self.OnEnter=self.OnEnter
        image = copy.deepcopy(self)
        return image
        
    def setOnEnter(self, onEnter):
        self.OnEnter=onEnter
        
    def setOnExit(self, OnExit):
        self.OnExit=OnExit    
   
    def __str__(self):
        OnEnter =""
        if (self.OnEnter!=""):
            OnEnter =f', OnEnter={self.OnEnter},'
            
        OnExit =""
        if (self.OnExit!=""):
            OnExit =f', OnExit={self.OnExit},'
            
        condition =""
        if (self.Condition!=""):
            condition =f', condition={self.Condition},'    
        handler = ""
        if (self.TransitionHandler!=""):
            handler = f'TransitionHandler={self.TransitionHandler}, '
        comment=""    
        if (self.Comment!=""):
            comment = f'TransitionHandler={self.Comment}, '
            
        OnExitRaiseEvent=""    
        if (self.OnExitRaiseEvent!=""):
            OnExitRaiseEvent = f'OnExitRaiseEvent={self.OnExitRaiseEvent}, '    
        
        OnEntryRaiseEvent=""    
        if (self.OnEntryRaiseEvent!=""):
            OnEntryRaiseEvent = f'OnEntryRaiseEvent={self.OnEntryRaiseEvent}, '   
            
        st  = f'OriginalState={self.OriginalState}, '
        st += f'Event={self.Event},  {condition}'
        st += f'NewState={self.NewState}, '
        st += f'{handler} {OnExit} {OnEnter}  {comment} {OnEntryRaiseEvent} {OnExitRaiseEvent}'

        return st