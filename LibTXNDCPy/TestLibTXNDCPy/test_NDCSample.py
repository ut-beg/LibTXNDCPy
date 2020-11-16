import unittest
import NDCSample
from datetime import date

testTitle = "Test Title"
testAlternateTitle = "Test Alternate Title"
testAbstract = "Test abstract"
testDataType = "Sample"
testDatasetReferenceDate = date(2020, 1, 1)
testDate = date(2020, 2, 1)
testSupplementalInformation = "Supplemental information"
testBrowseGraphic = "http://www.beg.utexas.edu/browsgraphic/test.png"
testOnlineResource = "http://www.beg.utexas.edu/onlineresource/test.png"
testAlternateGeometry = "Alternate geometry explanation"

testLongitude = -97.0
testLatitude = 30.0

testCollectionID = "collectionID"

verticalExtentUnit = "m"
verticalExtentUnitNotAllowed = "uF"
verticalExtentTop = 0
verticalExtentBottom = 50

class Test_test_NDCSample(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(Test_test_NDCSample, self).__init__(*args, **kwargs)
        
         #create the sample to test.
        self.sample = NDCSample.NDCSample()
                
        #initialize the sample's properties.
        self.sample.title = testTitle
        self.sample.alternateTitle = testAlternateTitle
        self.sample.abstract = testAbstract
        self.sample.dataType = testDataType
        self.sample.datasetReferenceDate = testDatasetReferenceDate
        self.sample.supplementalInformation = testSupplementalInformation
        self.sample.coordinatesLongitude = testLongitude
        self.sample.coordinatesLatitude = testLatitude
        self.sample.collectionID = testCollectionID
        self.sample.alternateGeometry = testAlternateGeometry
        self.sample.browseGraphic = testBrowseGraphic
        self.sample.onlineResource = testOnlineResource
        self.sample.date = testDate
        self.sample.verticalExtentUnit = verticalExtentUnit
        self.sample.verticalExtentTop = verticalExtentTop
        self.sample.verticalExtentBottom = verticalExtentBottom
   
    def test_title(self):
        if(isinstance(self.sample.title, str) == False):
            self.fail("Title is not a string")
       
        if(self.sample.title != testTitle):
            self.fail("Title value not returned")
    
    def test_alternateTitle(self):
        if(isinstance(self.sample.alternateTitle, str) == False):
            self.fail("Alternate title is not a string")

        if(self.sample.alternateTitle != testAlternateTitle):
            self.fail("Alternate title value not returned")

    def test_abstract(self):
        if(isinstance(self.sample.abstract, str) == False):
            self.fail("Abstract is not a string")

        if(self.sample.abstract != testAbstract):
            self.fail("Abstract value not returned")

    def test_dataType(self):
        if(isinstance(self.sample.dataType, str) == False):
            self.fail("Data type is not a string")

        if(self.sample.dataType != testDataType):
            self.fail("Data type value not value")

    def test_supplementalInformation(self):
        if(isinstance(self.sample.supplementalInformation, str) == False):
            self.fail("Supplemental information is not a string")

        if(self.sample.supplementalInformation != testSupplementalInformation):
            self.fail("Supplemental information value not returned")

    def test_datasetReferenceDate(self):
        if(isinstance(self.sample.datasetReferenceDate, date) == False):
            self.fail("Dataset reference date is not a date")

        if(self.sample.datasetReferenceDate != testDatasetReferenceDate):
            self.fail("Dataset reference date value is not correct")

    def test_discreteCoordinates(self):
        if(isinstance(self.sample.coordinatesLatitude, float) == False):
            self.fail("Latitude value is not a float")

        if(isinstance(self.sample.coordinatesLongitude, float) == False):
            self.fail("Longitude is not a float")

        if(self.sample.coordinatesLatitude != testLatitude):
            self.fail("Latitude value is incorrect")

        if(self.sample.coordinatesLongitude != testLongitude):
            self.fail("Longitude value is incorrect")

    def test_coordinates(self):
        if(isinstance(self.sample.coordinates, str) == False):
            self.fail("coordinates is not a string.")

        testCoordinatesString = str(testLongitude) + "," + str(testLatitude)

        if(self.sample.coordinates != testCoordinatesString):
            self.fail("Coordinates value is not correct")
    
    def test_collectionID(self):
        if(isinstance(self.sample.collectionID, str) == False):
            self.fail("Collection ID is not a string")

        if(self.sample.collectionID != testCollectionID):
            self.fail("Collection ID value is incorrect")

    def test_alternateGeometry(self):
        if(isinstance(self.sample.alternateGeometry, str) == False):
            self.fail("Alternate geometry is not a string")

        if(self.sample.alternateGeometry != testAlternateGeometry):
            self.fail("Alternate geometry value is incorrect")

    def test_onlineResource(self):
        if(isinstance(self.sample.onlineResource, str) == False):
            self.fail("Online resource is not a string")

        if(self.sample.onlineResource != testOnlineResource):
            self.fail("Online resource value is incorrect")

        #Eventually need to test what happens when one tries to set this with a non-url

    def test_browseGraphic(self):
        if(isinstance(self.sample.browseGraphic, str) == False):
            self.fail("Browse graphic is not a string")

        if(self.sample.browseGraphic != testBrowseGraphic):
            self.fail("Browse graphic value is not correct")

    def test_date(self):
        if(isinstance(self.sample.date, date) == False):
            self.fail("Date is not a date.")

        if(self.sample.date != testDate):
            self.fail("Date value is incorrect")

    def test_verticalExtent(self): 
        if(self.sample.verticalExtentUnit != verticalExtentUnit):
            self.fail("Vertical extent unit is incorrect")

        if(self.sample.verticalExtentTop != verticalExtentTop):
            self.fail("Vertical extent top incorrect.  Expected: " + str(verticalExtentTop) + ", got " + str(self.sample.verticalExtentTop))

        if(self.sample.verticalExtentBottom != verticalExtentBottom):
            self.fail("Vertical extent bottom incorrect.  Expected: " + str(verticalExtentBottom) + ", got " + str(self.sample.verticalExtentBottom))

        if(self.sample.verticalExtent != "m,50,0"):
            self.fail("Vertical extent returns improper value.")

    def test_toNDCXml(self):
        
        xml = self.sample.toNDCXml()

        if xml == "":
            self.fail("XML should not be empty")

if __name__ == '__main__':
    unittest.main()
