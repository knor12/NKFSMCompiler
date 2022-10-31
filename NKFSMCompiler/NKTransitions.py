__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

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
        #remove states that are just an empty string    
        states = [x for x in states if x != ''] 
        return  states 

    def getEvents(self):
        events = []
        for transition in self.transitions:
            events.append(transition.Event)
        events = list(dict.fromkeys(events))   
        #remove events that are just an empty string    
        events = [x for x in events if x != '']         
        return  events 

    def getHandlers(self):
        handlers = []
        #append handlers
        for transition in self.transitions:
            handlers.append(transition.TransitionHandler)
            if transition.OnExit != "":
                handlers.append(transition.OnExit)

            if transition.OnEnter != "":
                handlers.append(transition.OnEnter)
        #remove duplicates        
        handlers = list(dict.fromkeys(handlers))
        #remove handlers that are just an empty string    
        handlers = [x for x in handlers if x != '']         
        return  handlers         
    
    def getConditions(self):
        conditions = []
        for transition in self.transitions:
            if (transition.Condition!=""):
                conditions.append(transition.Condition)
        conditions = list(dict.fromkeys(conditions)) 
        #remove conditions that are just an empty string    
        conditions = [x for x in conditions if x != '']        
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
   