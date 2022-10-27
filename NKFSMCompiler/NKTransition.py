__author__      = "Noreddine Kessa"
__copyright__   = "MIT License"

import NKTransition

class NKTransition:

    def __init__(self, OriginalState, Event, NewState , TransitionHandler):
        self.OriginalState =OriginalState
        self.Event = Event
        self.NewState = NewState 
        self.TransitionHandler = TransitionHandler.replace("\n" , "")
   
    def __str__(self):
        st = f'OriginalState={self.OriginalState}, Event={self.Event}, NewState={self.NewState}, TransitionHandler={self.TransitionHandler}'
        return st