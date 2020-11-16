# NDCGeophysicalLog.py - Aaron Averett - Bureau of Economic Geology, 2020
# This is a sample object representing a geophysical log, with fields for the type, scales, and so forth.

from NDCSampleFromOGWell import NDCSampleFromOGWell

class NDCGeophysicalLog(NDCSampleFromOGWell):
    """ Represents a geophysical log """

    def __init__(self):
        super().__init__()

        self.logTypes = None
        self.logScales = None
        self.maxRecordedTemperature1 = None
        self.maxRecordedTemperature2 = None
        self.maxRecordedTemperature3 = None

    @property
    def logTypes(self):
        """ This represents the type of log - BEG recommends a comma separated list. """
        return self.__logTypes

    @logTypes.setter
    def logTypes(self, val):
        self.__logTypes = val

    @property
    def logScales(self):
        """ This represents the scales of the log in inches per [hundred?] feet. """
        return self.__logScales

    @logScales.setter
    def logScales(self, val):
        self.__logScales = val

    @property
    def maxRecordedTemperature1(self):
        """ The first of three max recorded temperature values"""
        return self.__maxRecordedTemperature1

    @maxRecordedTemperature1.setter
    def maxRecordedTemperature1(self, val):
        self.__maxRecordedTemperature1 = val

    @property
    def maxRecordedTemperature2(self):
        """ The second of three max recorded temperature values. """
        return self.__maxRecordedTemperature2

    @maxRecordedTemperature2.setter
    def maxRecordedTemperature2(self, val):
        self.__maxRecordedTemperature2 = val

    @property
    def maxRecordedTemperature3(self):
        """ The third of three max recorded temperature values. """
        return self.__maxRecordedTemperature3

    @maxRecordedTemperature3.setter
    def maxRecordedTemperature3(self, val):
        self.__maxRecordedTemperature3 = val
