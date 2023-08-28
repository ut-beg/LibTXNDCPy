from LibTXReSciCollPy import RSCSampleFromOGWell

class RSCRockCoreSample(RSCSampleFromOGWell):
    """This is a type of sample that represents a core sample."""

    def __init__(self, *args, **kwargs): 
        super().__init__()
        self.dataType = "Rock Core"

        self.sampleTypeDesc = None
        self.formationName = None
        self.formationAge = None

    #This is the human-readable description of the sample type.  Unlike the "data type", it can be whatever we want.
    @property
    def sampleTypeDesc(self):
        return self.__sampleTypeDesc

    @sampleTypeDesc.setter
    def sampleTypeDesc(self, val):
        self.__sampleTypeDesc = val

    #The formation name property
    @property
    def formationName(self):
        return self.__formationName
    
    @formationName.setter
    def formationName(self, val):
        self.__formationName = val

    #The formation age property
    @property
    def formationAge(self):
        return self.__formationAge

    @formationAge.setter
    def formationAge(self, val):
        self.__formationAge = val

    def composeAbstractElements(self):
        ret = super().composeAbstractElements()

        self.addAbstractElement(self.sampleTypeDesc, "Sample Type", ret)
        self.addAbstractElement(self.formationName, "Formation", ret)
        self.addAbstractElement(self.formationAge, "Formation Age", ret)
        
        return ret

