import unittest
import os
from NDCconvertSamples import NDCSampleConverter

class Test_test_NDCconvertSamples(unittest.TestCase):
    def setUp(self):
        self.NDCSampleConverter = NDCSampleConverter(True)

        curpath = os.path.dirname(os.path.realpath(__file__))

        self.curpath = curpath
        
        #load the URLEncoded data to test with
        with open(curpath + '/testfiles/urlencoded.txt') as urlencodedreader:
            self.urlencodeddata = urlencodedreader.read()

    def test_loadFromUrlEncodedString(self):
        if(self.urlencodeddata == "" or self.urlencodeddata == None):
            self.fail("Urlencoded JSON data not loaded.  Got: " + str(self.urlencodeddata))

        self.NDCSampleConverter.loadFromUrlEncodedString(self.urlencodeddata)

        if(self.NDCSampleConverter.json == ""):
            self.fail("JSON should not be empty")

    def test_populateSamples(self):

        #Load up the urlencoded data from the 
        self.NDCSampleConverter.loadFromUrlEncodedString(self.urlencodeddata)

        self.NDCSampleConverter.populateSamples()

        if self.NDCSampleConverter.samples == None:
            self.fail("Converter samples should not be empty.")

    def test_loadFromFile(self):
        filepath = self.curpath + '/testfiles/samples.json'
        
        self.NDCSampleConverter.loadFromFile(filepath)
        
        if self.NDCSampleConverter.json == "":
            self.fail("JSON should not be empty")

    def test_populateSamples(self):
        filepath = self.curpath + '/testfiles/samples.json'
        
        self.NDCSampleConverter.loadFromFile(filepath)

        self.NDCSampleConverter.populateSamples()

        if(self.NDCSampleConverter.samples != None and 
           self.NDCSampleConverter.samples.samples.count != 2):
            self.fail("Incorrect number of samples")

    def tearDown(self):
        pass #We'll presumably need to do something here eventually

if __name__ == '__main__':
    unittest.main()
