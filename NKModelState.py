__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from NKModelState import *
from NKModelTransition import *

class NKSCXMLState: 


    def __init__(self):
        self.stateName =""
        self.stateFullName =""
        self.initialState =""
        self.subStates = []
        self.transitions = []
        self.onExitScript = ""
        self.onEntryScript = ""
        self.onEntryRaiseEvent = ""
        self.onExitRaiseEvent = ""
        self.comment = ""