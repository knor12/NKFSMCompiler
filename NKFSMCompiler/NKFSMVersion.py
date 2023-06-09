#Initial release
#VERSION = "V0.02"

#add user defined section to the SFM structure.
VERSION = "V0.03"

class NKFSMVersion:

    

    def __init__(self):
        self.version = f"{VERSION}"
        
    def getVersion(self):
        return f'{self.version}'