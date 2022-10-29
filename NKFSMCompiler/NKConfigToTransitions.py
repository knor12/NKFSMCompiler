__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from NKTransitions import *
from NKTransition import *


class NKConfigToTransitions:

    def __init__(self, ConfigPath=""):
        self.ConfigPath =ConfigPath
        self.transitions = NKTransitions(Name="" , initialState="" , errorSate ="")
        
        
    def read(self , ConfigPath):
        self.ConfigPath =ConfigPath    
        file1 = open(ConfigPath, 'r')
        Lines = file1.readlines()

        #Strips the newline character
        for line in Lines:
            print (f"Processing line:{line}")
            words = line.split(",")
            #process two words lines
            if len (words) >=2:
                if (words[0]=="$NAME"):
                    self.transitions.Name = words[1]
                elif (words[0]=="$INITIALSTATE"):
                    self.transitions.initialState = words[1]
                elif (words[0]=="$ERRORSTATE"):
                    self.transitions.errorSate = words[1]                
                    
            #process multiple words lines
            if len(words)>= 5:
                if (words[0]=="$TRANSITION"):
                    self.transitions.append(NKTransition(OriginalState=words[1], Event=words[2], NewState=words[3] , TransitionHandler=words[4], Condition=words[5], Comment=words[6]))
                    
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