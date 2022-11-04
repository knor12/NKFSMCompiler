__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from NKTransitions import *
from NKTransition import *
import xml.dom.minidom

class NKSCXMLToTransitions:

    def __init__(self, ConfigPath=""):
        self.SCXMLPath =ConfigPath
        self.transitions = NKTransitions(Name="" , initialState="" , errorSate ="")
        self.motherNodeAndSubNodes = {"":""}
        self.motherNodesNames=[]
        self.compositeInitial={"":""}
     
    
    def isSimpleState(self, stateNode): 
        states = stateNode.getElementsByTagName("state")
        if len(states) > 0:
            return False 

        return True
        
    def processSubStates(self, stateNode):
        
        #check if this is composite motherNode
        motherStateName = stateNode.getAttribute("id")
        motherStateInitial = stateNode.getAttribute("initial")
        self.compositeInitial[motherStateName]=f'{motherStateName}_{motherStateInitial}'
        states = stateNode.getElementsByTagName("state")
        subStateNames = []
        if len(states)<=0:
            return False #not a composite node
            
        OnEntryDic = {"":""}
        OnExitDic = {"":""}    
            
        for state in states:
            stateName= state.getAttribute("id")
            subStateNames.append(stateName)
            print (f'now processing {stateName} \n')
            
            onExits = state.getElementsByTagName("onexit")
            for onExit in onExits:
                scripts = onExit.getElementsByTagName("script")
                script = scripts[0]
                OnExitDic[stateName] = self.getText(script.childNodes)
                #print(f'on exit found {OnExitDic} \n')                 
            
            onEntrys = state.getElementsByTagName("onentry")
            for onEntry in onEntrys:
                scripts = onEntry.getElementsByTagName("script")
                script = scripts[0]
                OnEntryDic[stateName] = self.getText(script.childNodes)
                #print(f'on entry found {OnEntryDic} \n') 
        

 
            
        #process tranitions
        for state in states:
            if not self.isSimpleState(state):
                continue
            stateName= state.getAttribute("id")
            self.motherNodesNames.append(stateName)
            stateName=f'{motherStateName}_{stateName}'
            #find all transitions
            event=""
            target=""
            cond ="" 
            transitions = state.getElementsByTagName("transition")
            for trasition in transitions:
                event = trasition.getAttribute("event")
                target = trasition.getAttribute("target")
                cond = trasition.getAttribute("cond")
                callback=trasition.getAttribute("callback")
                comment=trasition.getAttribute("comment")
                tran = NKTransition(OriginalState=stateName, Event=event, NewState=target , TransitionHandler=callback, Condition=cond, Comment=comment)
                #tran.setOnExit(onExitName)
                #tran.setOnEnter(onEntryName)
                
                #check if this transition has onEntry routine
                if tran.NewState in OnEntryDic.keys():
                    tran.OnEnter = OnEntryDic[tran.NewState]
                
                #check if this transition has onExit routine   
                if tran.OriginalState in OnExitDic.keys():
                    tran.OnExit = OnExitDic[tran.OriginalState]
                    
                #add transition to the model
                self.transitions.append(tran) 
        
        
                #keep track of each node and its children
        self.motherNodeAndSubNodes[motherStateName] = subStateNames 
        print(f'motherNodeAndSubNodes={self.motherNodeAndSubNodes}===================================')
        return True; 
        
     

    def getText(self , nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)    
        
    def read(self , ConfigPath):
        self.SCXMLPath =ConfigPath 
        SCXMLPath =     ConfigPath    
        doc = xml.dom.minidom.parse(SCXMLPath);
        
        #check if have a valid file
        topeNodeName= doc.nodeName
        if not ("scxml" in topeNodeName):
            print (f"Error, {SCXMLPath} is not a valid scxml file\n")
            
        #get the name of the state machine
        topNode =""
        topNodes = doc.getElementsByTagName("scxml")
        for i  in topNodes:
            topNode = i 
            
            
        self.transitions.Name = topNode.getAttribute("name")
        self.transitions.initialState = topNode.getAttribute("initial")
        self.transitions.errorSate = topNode.getAttribute("error")
        
        #get all available states
        states = doc.getElementsByTagName("state")
        #get all onEntry and onExit script names, used later
        OnEntryDic = {"":""}
        OnExitDic = {"":""}
        for state in states:
            if not self.isSimpleState(state):
                continue
                
            stateName= state.getAttribute("id")
            print (f'now processing {stateName} \n')
            
            onExits = state.getElementsByTagName("onexit")
            for onExit in onExits:
                scripts = onExit.getElementsByTagName("script")
                script = scripts[0]
                OnExitDic[stateName] = self.getText(script.childNodes)
                #print(f'on exit found {OnExitDic} \n')                 
            
            onEntrys = state.getElementsByTagName("onentry")
            for onEntry in onEntrys:
                scripts = onEntry.getElementsByTagName("script")
                script = scripts[0]
                OnEntryDic[stateName] = self.getText(script.childNodes)
                #print(f'on entry found {OnEntryDic} \n')                
        
        #process tranitions
        for state in states:
            #see if this state is a composite
            if not self.isSimpleState(state):
                self.processSubStates(state)
                continue
                
            stateName= state.getAttribute("id")
            #find all transitions
            event=""
            target=""
            cond ="" 
            transitions = state.getElementsByTagName("transition")
            for trasition in transitions:
                event = trasition.getAttribute("event")
                target = trasition.getAttribute("target")
                cond = trasition.getAttribute("cond")
                callback=trasition.getAttribute("callback")
                comment=trasition.getAttribute("comment")
                tran = NKTransition(OriginalState=stateName, Event=event, NewState=target , TransitionHandler=callback, Condition=cond, Comment=comment)
                #tran.setOnExit(onExitName)
                #tran.setOnEnter(onEntryName)
                
                #check if this transition has onEntry routine
                if tran.NewState in OnEntryDic.keys():
                    tran.OnEnter = OnEntryDic[tran.NewState]
                
                #check if this transition has onExit routine   
                if tran.OriginalState in OnExitDic.keys():
                    tran.OnExit = OnExitDic[tran.OriginalState]
                    
                #add transition to the model
                transition = self.transitions.append(tran)  

        #states to each of the substate of that composite state
        for tran in self.transitions.transitions: 
            if tran.NewState in self.compositeInitial.keys():
                tran.NewState = self.compositeInitial[tran.NewState]
                
        #replace the name         

        #if no error state create your own error state
        if self.transitions.errorSate == "":
            self.transitions.errorSate = f'{self.transitions.Name}_ERROR_State'

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