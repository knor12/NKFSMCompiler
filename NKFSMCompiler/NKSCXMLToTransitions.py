__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from NKTransitions import *
from NKTransition import *
#import xml.dom.minidom
import xml.etree.ElementTree as ET

class NKSCXMLToTransitions:

    def __init__(self, ConfigPath=""):
        self.SCXMLPath =ConfigPath
        self.transitions = NKTransitions(Name="" , initialState="" , errorSate ="")
        self.ns = {"ns":'http://www.w3.org/2005/07/scxml'}
        self.scxmlSignature = "xmlns=\"http://www.w3.org/2005/07/scxml\""
        self.stateAndSubStates = {}
        self.StateAndInitialState = {}
        self.OnEntryDic = {}
        self.OnExitDic = {}
        self.OnEntryRaiseEventsDict = {}
        self.OnExitRaiseEventsDict = {}
       

    def getText(self , nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)  


    def isStateComposite(self, stateNode):        
        subStates = stateNode.findall('state')
        if len(subStates)>0:
            return True
            
        return False


    def processSubStates(self, stateNode):
    
        #useful variables
        #OnEntryDic = {}
        #OnExitDic = {}

        #if the state is not a composite of states, just return
        if not self.isStateComposite(stateNode):
            return
         
        #define get state name
        motherStateName =   stateNode.get("id")  
            
        #get the initial state
        initialState= stateNode.get("initial")
        initialState = f'{motherStateName}_{initialState}'
        if initialState == "":
            printf(f"composite states {motherStateName} doesn't have an initial state.\n")
            exit()
        
        #sub state name
        subStateNames=[]
        print (f'processing {motherStateName} substates')
        
        #get all substates
        subStates = stateNode.findall('state')
        
        #process all the substates
        for state in subStates:
            stateName= state.attrib["id"]
            stateName= f'{motherStateName}_{stateName}'
            subStateNames.append(stateName)
            print (f'now processing the state {stateName} \n')
            
            if (self.isStateComposite(state)):
                print(f"error in {stateName}, we do not support more than one level nesting, refactor your state machine")
                exit()
            
            
            onExit = state.find("./onexit/script")
            if not (onExit is  None):
                onExit = onExit.text
                if onExit !="":
                    self.OnExitDic[stateName] = onExit

            onExitRaiseEvent = state.find("./onexit/raise")
            if not (onExitRaiseEvent is  None):
                onExitRaiseEvent = onExitRaiseEvent.attrib["event"]
                print (f'now processing rasise event {onExitRaiseEvent} \n')
                if onExitRaiseEvent !="":
                    self.OnExitRaiseEventsDict[stateName] = onExitRaiseEvent                    
            
            onEntry = state.find("./onentry/script")
            if not (onEntry is  None):
                onEntry = onEntry.text
                self.OnEntryDic[stateName] = onEntry

                
            onEntryRaiseEvent = state.find("./onentry/raise")
            if not (onEntryRaiseEvent is  None):
                onEntryRaiseEvent = onEntryRaiseEvent.attrib["event"]
                print (f'now processing rasise event {onEntryRaiseEvent} \n')
                if onEntryRaiseEvent !="":
                    self.OnEntryRaiseEventsDict[stateName] = onEntryRaiseEvent                    
        
        #process tranitions
        for state in subStates:
            stateName= state.attrib["id"]
            stateName=f'{motherStateName}_{stateName}'
            #find all transitions
            event=""
            target=""
            cond ="" 
            transitions = state.findall("transition")
            for trasition in transitions:
                if "event" in trasition.attrib.keys():    
                    event = trasition.attrib["event"]
                if "target" in trasition.attrib.keys():
                    target = trasition.attrib["target"]
                    target = f'{motherStateName}_{target}'
                if "cond" in trasition.attrib.keys():
                    cond = trasition.attrib["cond"]
                
                callback= "" #trasition.get("ns:callback", ns)
                comment="" #trasition.get("ns:comment", ns)
                if target =="":
                    target = stateName
                tran = NKTransition(OriginalState=stateName, Event=event, NewState=target , TransitionHandler=callback, Condition=cond, Comment=comment)

                
                #check if this transition has onEntry routine
                #print (OnEntryDic)
                #tran.NewState
                if tran.NewState in self.OnEntryDic.keys():
                    tran.OnEnter = self.OnEntryDic[tran.NewState]
                
                #check if this transition has onExit routine   
                if tran.OriginalState in self.OnExitDic.keys():
                    tran.OnExit = self.OnExitDic[tran.OriginalState]
                    
                #add transition to the model
                self.transitions.append(tran)            
        
        self.stateAndSubStates[motherStateName]=subStateNames
        self.StateAndInitialState[motherStateName]= initialState   
            
        
    def read(self , ConfigPath):
        self.SCXMLPath =ConfigPath 
        SCXMLPath =     ConfigPath    
        ns = self.ns
        scxmlSignature = self.scxmlSignature
            

        
        #check if have a valid file
        #if not 'scxml' in root.tag:
        #    print (f"Error, {SCXMLPath} is not a valid scxml file\n ")
        #    exit()

        #read the content of the file
        with open(SCXMLPath, 'r',encoding='utf-8-sig') as file:
            data = file.read()
            
            
        #check if this is a valid scxml file
        #print(f'signature={scxmlSignature}')
        #print(data)
        if not ( scxmlSignature in data ): 
            print (f"Error, {SCXMLPath} is not a valid scxml file\n ")
            exit()            
            
            
        #remove name space from the string
        data = data.replace(scxmlSignature,"")
        #print(data)    
            
        #start the reader object    
        #tree = ET.parse(SCXMLPath);
        #root = tree.getroot()  
        root = ET.fromstring(data)
        #print(f'root tag={root.tag}')
        

          
        

  
        self.transitions.Name = root.get("name")
        print(f'state machine name={self.transitions.Name}\n')
        self.transitions.initialState = root.get("initial")
        print(f'state machine initial state={self.transitions.initialState}\n')
        self.transitions.errorSate = root.get('error')
        if self.transitions.errorSate== "None" or self.transitions.errorSate== "" or self.transitions.errorSate is None:
            self.transitions.errorSate = f'{self.transitions.Name}_Error_State'
        

            
        states = root.findall('state')
        #get all onEntry and onExit script names, used later
        for state in states:
            stateName= state.attrib["id"]
            print (f'now processing the state {stateName} \n')
            
            
            onExit = state.find("./onexit/script")
            if not (onExit is  None):
                onExit = onExit.text
                print (f'now processing on exit {onExit} \n')
                if onExit !="":
                    self.OnExitDic[stateName] = onExit 
                    
            onExitRaiseEvent = state.find("./onexit/raise")
            if not (onExitRaiseEvent is  None):
                onExitRaiseEvent = onExitRaiseEvent.attrib["event"]
                print (f'now processing raise event {onExitRaiseEvent} \n')
                if onExitRaiseEvent !="":
                    self.OnExitRaiseEventsDict[stateName] = onExitRaiseEvent
                    
            onEntry = state.find("./onentry/script")
            if not (onEntry is  None):
                onEntry = onEntry.text
                self.OnEntryDic[stateName] = onEntry

            onEntryRaiseEvent = state.find("./onentry/raise")
            if not (onEntryRaiseEvent is  None):
                onEntryRaiseEvent = onEntryRaiseEvent.attrib["event"]
                print (f'now processing rasise event {onEntryRaiseEvent} \n')
                if onEntryRaiseEvent !="":
                    self.OnEntryRaiseEventsDict[stateName] = onEntryRaiseEvent        

                
        
        #process tranitions
        for state in states:
            self.processSubStates(state)
            stateName= state.attrib["id"]
            #find all transitions

            transitions = state.findall("transition")
            for trasition in transitions:
                event=""
                target=""
                cond =""
                
                if "event" in trasition.attrib.keys():    
                    event = trasition.attrib["event"]
                if "target" in trasition.attrib.keys():
                    target = trasition.attrib["target"]
                if "cond" in trasition.attrib.keys():
                    cond = trasition.attrib["cond"]
                
                callback= "" #trasition.get("ns:callback", ns)
                comment="" #trasition.get("ns:comment", ns)
                if target == "":
                    target = stateName    
                tran = NKTransition(OriginalState=stateName, Event=event, NewState=target , TransitionHandler=callback, Condition=cond, Comment=comment)

                
                #check if this transition has onEntry routine
                if tran.NewState in self.OnEntryDic.keys():
                    tran.OnEnter = self.OnEntryDic[tran.NewState]
                    

                        
                
                #check if this transition has onExit routine   
                if tran.OriginalState in self.OnExitDic.keys():
                    tran.OnExit = self.OnExitDic[tran.OriginalState]   
                    
                #add transition to the model
                self.transitions.append(tran)  


        #if no error state create your own error state
        if self.transitions.errorSate == "":
            self.transitions.errorSate = f'{self.transitions.Name}_ERROR_State'
            
            
        #refactor access to inner states
        stateAndSubStates = self.stateAndSubStates
        StateAndInitialState =self.StateAndInitialState
        
                        
                   
        
        #send events sent to composite states to their initial states.
        for tran in self.transitions.transitions:
            #change mother as target to its initial state
            if tran.NewState in StateAndInitialState.keys():
                motherState =tran.NewState
                initialState= StateAndInitialState[motherState]    
                tran.NewState = initialState
                #add initial state to execute it onEntry function
                if initialState in self.OnEntryDic.keys():
                    tran.OnEnter = self.OnEntryDic[initialState]
                
        #for events going out from composite states to 
        #outside states, refactor them for all inner states
        for tran in self.transitions.transitions:
            if tran.OriginalState in stateAndSubStates.keys():
                motherState=tran.OriginalState
                SubStates= stateAndSubStates[motherState]
                counter_=0;
                #print(f'{SubStates}')    
                for subState in SubStates:
                    #only rename the first transition 
                    if counter_ == 0: 
                        tran.OriginalState = subState
                        if subState in self.OnExitDic.keys():
                            tran.OnExit = self.OnExitDic[subState]
                    else:   
                        image = tran.clone()
                        image.OriginalState = subState
                        if subState in self.OnExitDic.keys():
                            image.OnExit = self.OnExitDic[subState]
                        self.transitions.append(image)
                    counter_+=1

        #change all sub states names to the name that reflects their parents names as well
        #for tran in self.transitions.transitions:
        #    for motherState in stateAndSubStates.keys():
        #        for subState in stateAndSubStates[motherState]:
        #            if tran.OriginalState ==subState:
        #                tran.OriginalState = f'{motherState}_{tran.OriginalState}'
        #            if tran.NewState ==subState:
        #                tran.NewState = f'{motherState}_{tran.NewState}'
                        
        # if the initial state of top level a composite state, change the overall initial state to that of the coposite
        if self.transitions.initialState in StateAndInitialState.keys():        
            self.transitions.initialState = StateAndInitialState[self.transitions.initialState]
            
        #resolve all the rased events
        print (f'exit raise events {self.OnExitRaiseEventsDict}')
        print (f'entry raise events {self.OnEntryRaiseEventsDict}')
        for tran in self.transitions.transitions:    
            #check if this state has a raise event on exit
            if tran.OriginalState in self.OnExitRaiseEventsDict.keys():
                tran.OnExitRaiseEvent = self.OnExitRaiseEventsDict[tran.OriginalState]
            #check if this state has a raise event on entry
            if tran.NewState in self.OnEntryRaiseEventsDict.keys():
                tran.OnEntryRaiseEvent = self.OnEntryRaiseEventsDict[tran.NewState]             
        
        print (f"stateAndSubStates={self.stateAndSubStates}\n" )
        print (f"StateAndInitialState={self.StateAndInitialState}\n" )        

        if (self.transitions.Name==""):
            print("Error: $NAME not defind\n")
            return False
            
        if (self.transitions.initialState==""):
            print("Error: $INITIALSTATE not defind\n")
            return False

            
        if (self.transitions.errorSate==""):
            print("Error: $ERRORSTATE not defind\n")
            return False    
        
        if len(self.transitions.transitions) <1:
            print("Error: $TRANSITION not defind\n")
            return False
        return True        
            
    def getTransitions(self):
        return self.transitions
        
        
        
if __name__ == "__main__":
#some test code
    SCXMLPath = "./state.scxml"
    reader = NKSCXMLToTransitions() 
    
    reader.read(SCXMLPath)
    tran  = reader.getTransitions()  
    print(f'{tran} done')    