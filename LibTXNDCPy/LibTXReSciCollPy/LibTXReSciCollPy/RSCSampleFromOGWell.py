from LibTXReSciCollPy import RSCSample

class RSCSampleFromOGWell(RSCSample):
    
    """This represents a sample of some kind that comes from an oil and/or gas well.  It has properties such as the API number and operator that get integrated into the abstract field for export."""

    def __init__(self):
        super().__init__()

        self.apiNumber = None
        self.leaseName = None
        self.wellNumber = None
        self.stateName = None
        self.countyName = None
        self.countryName = None
        self.fieldName = None
        self.operatorName = None

    @property
    def apiNumber(self):
        """ API number for the well the sample comes from """
        return self.__apiNumber

    @apiNumber.setter
    def apiNumber(self, val):
        self.__apiNumber = val

    @property
    def leaseName(self):
        """ Lease name for the well the sample comes from.   Generally, combine this with the well number and you get the 'well name'"""
        return self.__leaseName

    @leaseName.setter
    def leaseName(self, val):
        self.__leaseName = val

    @property
    def wellNumber(self):
        """ Well number for the well the sample comes from.  Generally, combine this with the lease name and you get the 'well name' """
        return self.__wellNumber

    @wellNumber.setter
    def wellNumber(self, val):
        self.__wellNumber = val

    @property
    def stateName(self):
        """ The name of the state or province where the well the sample comes from is located. """
        return self.__stateName

    @stateName.setter
    def stateName(self, val):
        self.__stateName = val

    @property
    def countyName(self):
        """ The name of the county/parish where the well the sample comes from is located """
        return self.__countyName

    @countyName.setter
    def countyName(self, val):
        self.__countyName = val

    @property
    def countryName(self):
        """ The name of the country where the well the sample comes from is located """
        return self.__countryName

    @countryName.setter
    def countryName(self, val):
        self.__countryName = val
        
    @property
    def fieldName(self):
        """ The field name for the well where the sample came from """
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, val):
        self.__fieldName = val

    @property 
    def operatorName(self):
        """ The operator name from the well the sample comes from """
        return self.__operatorName

    @operatorName.setter
    def operatorName(self, val):
        self.__operatorName = val

    def composeAbstractElements(self):
        """ Returns a list of strings, each representing a line in the final abstract value """
        ret = super().composeAbstractElements()

        #tack our abstract elements on to the list.
        self.addAbstractElement(self.apiNumber, "API Number", ret)
        self.addAbstractElement(self.leaseName, "Lease Name", ret)
        self.addAbstractElement(self.wellNumber, "Well Number", ret)
        self.addAbstractElement(self.countyName, "County Name", ret)
        self.addAbstractElement(self.stateName, "State Name", ret)
        self.addAbstractElement(self.countryName, "Country Name", ret)
        self.addAbstractElement(self.fieldName, "Field Name", ret)
        self.addAbstractElement(self.operatorName, "Operator Name", ret)

        return ret




