
from NDCRockCoreSample import NDCRockCoreSample
from NDCSamples import NDCSamples
from datetime import date


testfilePath = '../../Auxiliary/NDC_XML_file_example.xml'
outfilePath = '../../Auxiliary/testout.xml'

samples = NDCSamples()

rcs1 = NDCRockCoreSample()

rcs1.title = "Test Title"
rcs1.coordinatesLatitude = 32.0
rcs1.coordinatesLongitude = -98.0
rcs1.supplementalInformation = "Sample ID 0 - Bureau of Economic Geology Core Research Center, 10100 Burnet Rd., Austin, TX 78758, 512-475-9561"
rcs1.datasetReferenceDate = date.today()

rcs1.apiNumber = "1111111111"
rcs1.internalReferenceNumber1Description = "Sample ID"
rcs1.internalReferenceNumber1 = "0"
rcs1.internalReferenceNumber2Description = "Accession Number"
rcs1.internalReferenceNumber2 = "C000001"
rcs1.formationName = "Eagle Ford"
rcs1.date = date.today()

samples.addSample(rcs1)

xmlText = samples.toNDCXmlString()

print(xmlText)