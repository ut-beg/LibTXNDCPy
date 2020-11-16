# NDCSampleFactory.py - Aaron Averett - Bureau of Economic Geology, 2020
# This is a helper for NDCconvertSamples.py.  It encapsulates the logic required to convert whatever the input data is to our data model,
# so that we can then export it to our XML format.

from NDCSample import NDCSample
from NDCSampleFromOGWell import NDCSampleFromOGWell
from NDCRockCoreSample import NDCRockCoreSample
from NDCGeophysicalLog import NDCGeophysicalLog
from NDCSamples import NDCSamples
import json

class NDCSampleFactory(object):
    """This object accepts a set of JSON data and instantiates a corresponding sample object of the appropriate type."""

    def __init__(self):

        #Initialize the allowed classes with our built-in ones.
        self.allowedClasses = {
                "Sample": NDCSample,
                "SampleFromOGWell": NDCSampleFromOGWell,
                "RockCoreSample": NDCRockCoreSample,
                "GeophysicalLog": NDCGeophysicalLog
            }

    #Adds a class to the set of allowed classes.
    def addAllowedClass(self, classKey, objectClass):
        self.allowedClasses[classKey] = objectClass;

    #Creates a sample object of the given type
    def createSample(self, classKey):
        ret = None

        if self.allowedClasses[classKey] != None:
            #create the object instance
            ret = self.allowedClasses[classKey]()
            
        return ret

    #Populates the properties of the sample object with the given values
    def populateSample(self, sample, contents):
        jsonContent = json.loads(contents)

        for key in jsonContent:
            value = jsonContent[key]

            if hasattr(sample, key):
                sample[key] = value

    #Populates the 
    def createPopulatedSample(self, classKey, contents):
        
        sample = self.createSample(classKey)

        self.populateSample(contents)

        return sample

    def createSamplesWithJson(self, contents):
        
        jsonContent = json.loads(contents)
        samples = NDCSamples()

        for jsample in jsonContent["samples"]:
            newsample = self.createSample(jsample['classKey'])
            
            for key in jsample:
                if key != 'classKey':
                    setattr(newsample, key, jsample[key])

            samples.addSample(newsample)

        return samples
