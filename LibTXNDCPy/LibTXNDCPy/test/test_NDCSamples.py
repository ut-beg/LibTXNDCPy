from NDCSample import NDCSample
from NDCSamples import NDCSamples
from datetime import date
import unittest
from NGGDPPTypes import samples

class Test_test_NDCSamples(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(Test_test_NDCSamples, self).__init__(*args, **kwargs)
        
        self.samples = NDCSamples()

        self.testSample1 = NDCSample()
        self.testSample2 = NDCSample()

    def test_addSample(self):
        numSamples = len(self.samples.samples)
        self.samples.addSample(self.testSample1)

        if(len(self.samples.samples) != numSamples + 1):
            self.fail("Incorrect sample set length after attempted add.")

    def test_removeSample(self):     
        self.samples.addSample(self.testSample2)

        numSamples = len(self.samples.samples)

        self.samples.removeSample(self.testSample2)

        if(len(self.samples.samples) + 1 != numSamples):
            self.fail("Incorrect sample set length after attempted removal.")

    def test_toNDCXml(self):
        xml = self.samples.toNDCXml()

        if not isinstance(xml, samples):
            self.fail("Expected an NGGDPP XML Samples type.  Got something else.")
            

if __name__ == '__main__':
    unittest.main()
