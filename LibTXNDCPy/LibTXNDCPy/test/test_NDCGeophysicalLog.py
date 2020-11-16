import unittest
from NDCGeophysicalLog import NDCGeophysicalLog

logTypes = "R,DI"
logScales = "1,2,5"
maxRecordedTemperature1 = 100
maxRecordedTemperature2 = 102
maxRecordedTemperature3 = 104

class Test_test_NDCGeophysicalLog(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_test_NDCGeophysicalLog, self).__init__(*args, **kwargs)

        self.rcs = NDCGeophysicalLog()

        self.rcs.logTypes = logTypes
        self.rcs.logScales = logScales
        self.rcs.maxRecordedTemperature1 = maxRecordedTemperature1
        self.rcs.maxRecordedTemperature2 = maxRecordedTemperature2
        self.rcs.maxRecordedTemperature3 = maxRecordedTemperature3

    def test_logTypes(self):
        self.failIfEqual(self.rcs.logTypes, None, "Log types should not be null")
        self.failIf((self.rcs.logTypes != logTypes), "Log types value is not correct.")
    
    def test_logScales(self):
        self.failIfEqual(self.rcs.logScales, None, "Log scales should not be null")
        self.failIf((self.rcs.logScales != logScales), "Log scales value is not correct")

if __name__ == '__main__':
    unittest.main()
