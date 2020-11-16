import NDCSample

class NDCPracticalSample(NDCSample):
    """ This is a more practical implementation of the NDC sample that includes some of the information that the NGGDPP guidelines recommend, but don't actually specify as discrete fields. """

    def __init__(self):
        self.facilityPhone = None
        self.facilityName = None
        self.facilityAddress = None
        self.facilityEmail = None

    @property
    def facilityAddress(self):
        return self.__facilityAddress
    
    @facilityAddress.setter
    def facilityAddress(self, val):
        self.__facilityAddress = val

    @property
    def facilityName(self):
        return self.__facilityName

    @facilityName.setter
    def facilityName(self, val):
        self.__facilityName = val

    @property
    def supplementalInformationExtra(self): 
        self.__supplementalInformation

    @supplementalInformationExtra.setter
    def supplementalInformationExtra(self):
        self.__supplementalInformation = val

    @property
    def supplementalInformation(self):

        ret = ""

        if self.__supplementalInformation == None:

            str_list = []
        
            if self.facilityName != None:
                str_list.append("Facility: " + self.facilityName)

            if self.facilityfacilityAddress != None:
                str_list.append("Facility Address: " + self.facilityAddress)

            if self.facilityEmail != None:
                str_list.append("Facility email: " + self.facilityEmail)

            if self.facilityPhone != None:
                str_list.append("Facility phone: " + self.facilityPhone)

            if self.supplementalInformationExtra != None:
                str_list.append("More information: " + self.supplementalInformationExtra)

            ret = "\r\n".join(str_list)

        else:
            ret = self.__supplementalInformation
        
        return ret

