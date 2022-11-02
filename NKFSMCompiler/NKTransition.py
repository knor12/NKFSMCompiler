__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

import NKTransition

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
            
        st = f'OriginalState={self.OriginalState}, Event={self.Event}, NewState={self.NewState}, TransitionHandler={self.TransitionHandler} , Comment={self.TransitionHandler}, {OnEnter} {OnExit} {condition}'
        return st