__author__      = "Noreddine Kessa"
__copyright__   = "MIT License"

from NKTransition import *
class NKTransitions:

    def __init__(self, Name , initialState, errorSate):
        self.Name =Name
        self.transitions=[]
        self.initialState=initialState
        self.errorSate=errorSate
        self.events=[]
        self.states=[]
        
    def append(self , transition):
        self.transitions.append(transition)  
        
        
    def getStates(self):
        states = []
        
        for transition in self.transitions:
            states.append(transition.OriginalState)
            states.append(transition.NewState)
        states.append(self.errorSate)
        states = list(dict.fromkeys(states))                
        return  states 

    def getEvents(self):
        events = []
        for transition in self.transitions:
            events.append(transition.Event)
        events = list(dict.fromkeys(events))     
        return  events 

    def getHandlers(self):
        handlers = []
        for transition in self.transitions:
            handlers.append(transition.TransitionHandler)
        handlers = list(dict.fromkeys(handlers))     
        return  handlers         
    
    def getConditions(self):
        conditions = []
        for transition in self.transitions:
            if (transition.Condition!=""):
                conditions.append(transition.Condition)
        conditions = list(dict.fromkeys(conditions))     
        return  conditions    

    def __str__(self):
        Events=self.getEvents()
        States=self.getStates()
        Handlers=self.getHandlers()
        Conditions = self.getConditions()
        st =f'Name={self.Name} \n'
        st+=f'Initial State={self.initialState}\n'
        st+=f'Error State={self.errorSate}\n'
        st+=f'States={States}\n'
        st+=f'Handlers={Handlers}\n'
        st+=f'Events={Events}\n\n'
        st+=f'conditions={Conditions}\n\n'
        for transition in self.transitions:
            st +=f'Transition={transition}\n'
        return st
   