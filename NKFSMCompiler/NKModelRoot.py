__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from NKModelState import *
from NKModelTransition import *
import xml.etree.ElementTree as ET

class NKRootModel: 


    def __init__(self):
       self.SCXMLPath =""
       self.scxmlSignature = "xmlns=\"http://www.w3.org/2005/07/scxml\""
       self.Name=""
       self.stateName=""
       self.stateFullName=""
       self.initialState=""
       self.errorStateName =""
       self.subStates=[]
       self.transitions=[]
       self.errorState="errorState"
       
       
    def   getHandlers(self):
        li = []
        for tran in self.transitions:
            temp = tran.TransitionHandler
            if temp !="": 
                li.append(temp)
            temp = tran.OnExit
            if temp !="": 
                li.append(temp)
            temp = tran.OnEnter
            if temp !="": 
                li.append(temp)
                
        #remove  duplicates and empty spaces        
        li = list(dict.fromkeys(li))        
        li = [x for x in li if x != '']
        return li
       
    def  getStates(self):
        li = []
        li.append(self.errorState)
        for tran in self.transitions:
            li.append(tran.OriginalState)
            li.append(tran.NewState)
 
                
        #remove  duplicates and empty spaces        
        li = list(dict.fromkeys(li))        
        li = [x for x in li if x != '']
        return li       
        
    def   getEvents(self):
        li = []
        for tran in self.transitions:
            li.append(tran.Event)
            if tran.OnExitRaiseEvent !="":
                li.append(tran.OnExitRaiseEvent)
            if tran.OnEntryRaiseEvent !="":
                li.append(tran.OnEntryRaiseEvent)
                
        #remove  duplicates and empty spaces        
        li = list(dict.fromkeys(li))        
        li = [x for x in li if x != '']
        return li        
       
    def getOnEntryFunctions(self, root):
        dictionary ={}
        for state in  root.subStates:
            if state.OnEnter !="" and  state.OnEnter != None:
                dictionary[state.stateName]=state.onEntryScript
            if len(state.subStates)>0:
                dictionary1=self.getOnEntryFunctions(state)
                dictionary.update(dictionary1)
                 
        return   dictionary   
       
    def getOnEntryRaiseEvents(self, root):
        dictionary ={}
        for state in  root.subStates:
            if state.onEntryRaiseEvent !="" and  state.onEntryRaiseEvent != None:
                dictionary[state.stateName]=state.onEntryScript
            if len(state.subStates)>0:
                dictionary1=self.getOnEntryRaiseEvent(state)
                dictionary.update(dictionary1)
                 
        return   dictionary  
        
    def __getStates(self, root):
        dictionary ={}
        #print("__getStates called")
        for state in  root.subStates:
            #print (f"processing {state.stateName}, {state.stateFullName} ")
            dictionary[state.stateName]=state.stateFullName
            if len(state.subStates)>0:
                dictionary1 = self.__getStates(state)
                dictionary.update(dictionary1)
        return dictionary
        
    def getSubStates(self,root, stateName):
            if stateName == root.stateName or stateName == root.stateFullName:
                return root.subStates
            for state in  root.subStates:
                lst = self.getSubStates(state,stateName )
                if len(lst)>0:
                    return lst
            return []

    def getStateOnEntryFunction(self,root, stateName):
            s=""
            for state in  root.subStates:
                if stateName == state.stateName or stateName == state.stateFullName:
                    return state.onEntryScript
                if len(state.subStates)>0:
                    s=self.getStateOnEntryFunction(state, stateName)
                    if s!="":
                        return s
                    
                    
            return "" 
            
    def getStateOnEntryRaiseEvent(self,root, stateName):
            s=""
            for state in  root.subStates:
                if stateName == state.stateName or stateName == state.stateFullName:
                    return state.onEntryRaiseEvent
                if len(state.subStates)>0:
                    s=self.getStateOnEntryRaiseEvent(state, stateName)
                    if s!="":
                        return s
                    
                    
            return ""       
 
    def getStateOnExitRaiseEvent(self,root, stateName):
            s=""
            for state in  root.subStates:
                if stateName == state.stateName or stateName == state.stateFullName:
                    return state.onExitRaiseEvent
                if len(state.subStates)>0:
                    s=self.getStateOnExitRaiseEvent(state, stateName)
                    if s!="":
                        return s
                    
                    
            return "" 
 
    def getStateOnExitFunction(self,root, stateName):
            s=""
            for state in  root.subStates:
                if stateName == state.stateName or stateName == state.stateFullName:
                    return state.onExitScript
                if len(state.subStates)>0:
                    s=self.getStateOnExitFunction(state, stateName)
                    if s!="":
                        return s
                    
                    
            return "" 
 
 
    def getinitialStates(self, root):
        dictionary ={}
        for state in  root.subStates:
            if state.initialState !="":
                dictionary[state.stateName]=state.initialState
                dictionary[state.stateFullName]=state.initialState
            if len(state.subStates)>0:
                dictionary1 = self.getinitialStates(state)
                dictionary.update(dictionary1)
        return dictionary
        
        
    def ____getTransitionsFromStates(self, root):
        l1 = []
        for state in  root.subStates:
            for i in state.transitions:
                l1.append(i)
            if len(state.subStates)>0:
                l2 = self.____getTransitionsFromStates(state)
                for i in l2:
                    l1.append(i)
                
        #print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')  
        #for i in l1: 
        #    print (f'{i}\n')   
        #print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')    
        return l1
    
    def __getTransitions(self, root):

        l1 = self.____getTransitionsFromStates(self)
        
        #for the events that are going to composite state send them to init state
        initialStates = self.getinitialStates(self)
        #print(f"initial states dictionary {initialStates}")
        count = 10
        while count > 0: #keep doing it untill you resolve all nested states
            count-=1
            for tran in l1:
                if tran.NewState in initialStates.keys():
                    tran.NewState = initialStates[tran.NewState]
            
            #process the overall initialization state
            if self.initialState in initialStates.keys():
                self.initialState = initialStates[self.initialState]
                
        #make sure we have an init state
        print (f"init state={self.initialState}")    
                    
                  
        #all transitions from composite states propagate them to each of their children states
        states = self.__getStates(self)
        done = False
        while not done:
            done = True
        for state in   states:
            for tran in l1:
                if tran.OriginalState in states.keys():
                    subStates = self.getSubStates(self,tran.OriginalState )
                    #print(f"sub states for {tran.OriginalState } are {subStates}")
                    counter = 0
                    for subState in subStates:
                        if counter ==0:
                            counter = 1
                            tran.OriginalState = subState.stateName
                            done = False
                        else: 
                            clone = tran.clone()
                            clone.OriginalState = subState.stateName
                            l1.append(clone)
                            
        #change all state names to their stateFullName
        for tran in l1:
            if tran.OriginalState in states.keys():
                tran.OriginalState = states[tran.OriginalState]
            if tran.NewState in states.keys():
                tran.NewState = states[tran.NewState]
                
        #add entry raise events, and entry functions
        for tran in l1:
            tran.OnEnter = self.getStateOnEntryFunction(self, tran.NewState)
            tran.OnEntryRaiseEvent = self.getStateOnEntryRaiseEvent(self, tran.NewState)
            tran.OnExit = self.getStateOnExitFunction(self, tran.OriginalState)
            tran.OnExitRaiseEvent = self.getStateOnExitRaiseEvent(self, tran.OriginalState)
        
        
        s=""
        for i in l1:
            self.transitions.append(i)
            s+= f'{self.transitions}\n'
            
        
        return s        
    
    #check if current state is composite of states
    def isStateComposite(self, stateNode):        
        subStates = stateNode.findall('state')
        if len(subStates)>0:
            return True    
        return False

    #process substates
    def readSubStates(self, SCXMLMotherState, motherModelState):

        #get all states from the top level    
        states = SCXMLMotherState.findall('state')
        for SCXMLstate in states:
        
            #read and store state data
            modelState = NKSCXMLState()
            
            modelState.stateName = SCXMLstate.attrib["id"]
            modelState.stateFullName =f'{motherModelState.stateFullName}_{modelState.stateName}'
            print (f'processing state {modelState.stateName}\n')
            if "initial" in SCXMLstate.attrib.keys():
                modelState.initialState = SCXMLstate.attrib["initial"]
                modelState.initialState = f'{modelState.stateFullName}_{modelState.initialState}'
                #print(f'after initial {modelState.initialState}')
                
            
            temp = SCXMLstate.find("./onexit/script")
            if not (temp is  None):
                modelState.onExitScript = temp.text
                #print(f'on exit handler {modelState.onExitScript}')
            
            temp = SCXMLstate.find("./onentry/script")
            if not (temp is  None):
                modelState.onEntryScript = temp.text
                #print(f'on entry handler {modelState.onEntryScript}')
                
            temp = SCXMLstate.find("./onentry/raise")
            if not (temp is  None):
                modelState.onEntryRaiseEvent = temp.attrib["event"]
                #print(f'on entry event {modelState.onEntryRaiseEvent}')
                
            temp =SCXMLstate.find("./onexit/raise")
            if not (temp is  None):
                modelState.onExitRaiseEvent = temp.attrib["event"]
                #print(f'on exit event {modelState.onExitRaiseEvent}')
                
            modelState.comment =""
            
            #find all transitions
            transitions = SCXMLstate.findall("transition")            
            for trasition in transitions:
                OriginalState = modelState.stateName #OK
                event="" #OK
                NewState = "" #
                cond ="" #OK
                NewState="" #ok
                OnExit = modelState.onExitScript #OK
                OnExitRaiseEvent = modelState.onExitRaiseEvent #OK
                OnEnter="" #TODO
                OnEntryRaiseEvent = "" #TODO
                
                if "event" in trasition.attrib.keys():    
                    event = trasition.attrib["event"]
                if "target" in trasition.attrib.keys():
                    NewState = trasition.attrib["target"]
                if "cond" in trasition.attrib.keys():
                    cond = trasition.attrib["cond"]
                    
                #check if staying in the same state
                if NewState == "":
                    NewState = OriginalState
                
                transitionModel =NKModelTransition()
                transitionModel.OriginalState =OriginalState
                transitionModel.Event = event
                transitionModel.NewState = NewState 
                transitionModel.Condition = cond
                transitionModel.TransitionHandler = ""
                transitionModel.Comment = ""
                transitionModel.OnExit=OnExit
                transitionModel.OnEnter=""
                transitionModel.OnExitRaiseEvent = OnExitRaiseEvent
                transitionModel.OnEntryRaiseEvent = ""
                
                #append the transitions to the list
                modelState.transitions.append(transitionModel)
            
            #add  state to list
            #print(f'enqueng {modelState.stateName}')
            motherModelState.subStates.append(modelState)
            
            #process sub states
            if self.isStateComposite(SCXMLstate): 
                self.readSubStates(SCXMLstate, modelState)
       
    def read(self, ConfigPath):
        SCXMLFilePath=ConfigPath
        #read the content of the file
        with open(SCXMLFilePath, 'r',encoding='utf-8-sig') as file:
            data = file.read()

        #check if this is a valid scxml file
        #print(f'signature={scxmlSignature}')
        #print(data)
        scxmlSignature =self.scxmlSignature
        if not ( scxmlSignature in data ): 
            print (f"Error, {SCXMLPath} is not a valid scxml file\n ")
            exit()        
        
        #remove name space from the string
        data = data.replace(scxmlSignature,"")
        #print(data)        
        
        #start the reader object    
        root = ET.fromstring(data)

        #get the state machine name
        self.Name = root.get("name")
        self.stateName=self.Name
        self.stateFullName=self.Name
        self.initialState = root.get("initial")
        
        self.errorSate=f'{self.Name}_errorState'
        
        #assign an error state name
        self.errorState = f'{self.Name}_errorState'


        #get all states from the top level    
        states = root.findall('state')
        #print(f'states{states}')
        for SCXMLstate in states:
            
        
            #read and store state data
            modelState = NKSCXMLState()
            
            
            modelState.stateName = SCXMLstate.attrib["id"]
            modelState.stateFullName =f'{self.Name}_{modelState.stateName}'
            print (f'processing state {modelState.stateName}\n')
            if "initial" in SCXMLstate.attrib.keys():
                modelState.initialState = SCXMLstate.attrib["initial"]
                modelState.initialState = f'{modelState.stateFullName}_{modelState.initialState}'
                
            
            temp = SCXMLstate.find("./onexit/script")
            if not (temp is  None):
                modelState.onExitScript = temp.text
            
            temp = SCXMLstate.find("./onentry/script")
            if not (temp is  None):
                modelState.onEntryScript = temp.text
                
            temp = SCXMLstate.find("./onentry/raise")
            if not (temp is  None):
                modelState.onEntryRaiseEvent = temp.attrib["event"]
                
            temp =SCXMLstate.find("./onexit/raise")
            if not (temp is  None):
                modelState.onExitRaiseEvent = temp.attrib["event"]
        
            modelState.comment =""  

            #find all transitions
            transitions = SCXMLstate.findall("transition")            
            for trasition in transitions:
                OriginalState = modelState.stateName #OK
                event="" #OK
                NewState = "" #
                cond ="" #OK
                NewState="" #ok
                OnExit = modelState.onExitScript #OK
                OnExitRaiseEvent = modelState.onExitRaiseEvent #OK
                OnEnter="" #TODO
                OnEntryRaiseEvent = "" #TODO
                
                if "event" in trasition.attrib.keys():    
                    event = trasition.attrib["event"]
                if "target" in trasition.attrib.keys():
                    NewState = trasition.attrib["target"]
                if "cond" in trasition.attrib.keys():
                    cond = trasition.attrib["cond"]
                    
                #check if staying in the same state
                if NewState == "":
                    NewState = OriginalState                    
                transitionModel = NKModelTransition()
                transitionModel.OriginalState =OriginalState
                transitionModel.Event = event
                transitionModel.NewState = NewState 
                transitionModel.Condition = cond
                transitionModel.TransitionHandler = ""
                transitionModel.Comment = ""
                transitionModel.OnExit=OnExit
                transitionModel.OnEnter=""
                transitionModel.OnExitRaiseEvent = OnExitRaiseEvent
                transitionModel.OnEntryRaiseEvent = ""
                
                #append the transitions
                modelState.transitions.append(transitionModel)
                
            
            

            
            #process sub states
            #print(f'full name {modelState.stateFullName}')
            if self.isStateComposite(SCXMLstate): 
                self.readSubStates(SCXMLstate, modelState)
                
            #add to list
            
            self.subStates.append(modelState) 
            #print(f'enqueng {self.subStates}')


        #process all transitions
        s= self.__getTransitions(self)
        print ("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n")
        print(self)
        print ("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n")
        return True    
            
        
        
    def __str__(self):
        s=  f'states={self.__getStates(self)}\n\n\n'
        s=  f'Initial states={self.getinitialStates(self)}\n\n\n'
        s=""
        for i in self.transitions:
            s+=f'transitions={i}\n\n'
        return s
        
        
if __name__ == "__main__":

    model =   NKRootModel()
    model.read (ConfigPath="./TraficLight.scxml")
    print(f'{model}')    