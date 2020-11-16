# LibTXNDCPy
A Python library and some C# wrappers for generating the XML format required by USGS's [National Geological and Geophysical Data Preservation Program's](https://www.usgs.gov/core-science-systems/national-geological-and-geophysical-data-preservation-program) (NGGDPP) "National Digital Catalog" of geological sample materials.

One of the difficulties faced by state geological surveys participating in the National Geological and Geophysical Data Preservation Program is the need to submit metadata back to USGS's National Digital Catalog (NDC) in a particular XML schema.  XML can be difficult to generate, as the code required to do so programmatically is often complex and verbose.  LibTXNDCPy addresses this difficulty by providing a simple API for populating this XML format.  Also provided are a command line launcher for usage either as a standalone converter or launching from languages that do not natively integrate with Python, and C# wrapper and interface library, which the Bureau of Economic Geology uses to interface with its own internal geologic materials database.

## Python Quick Start:
Install LibTXNDCPy:
```
pip install LibTXNDCPy
```

Use LibTXNDCPy in your code:
```
from LibTXNDCPy import NDCSamples
from LibTXNDCPy import NDCRockCoreSample

#In the NDC XML schema, <samples></samples> is the container used to hold a set of sample objects
samples = NDCSamples()

#Create a sample object.  This one has fields for the Bureau of Economic Geology's definition of a rock core.
rcs1 = NDCRockCoreSample()

#Populate the sample object with at least the minimum set of data.
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

#Add the sample to the samples object.
samples.addSample(rcs1)

#Convert the sample object to the XML data.
xmlText = samples.toNDCXmlString()

#Do something with the excel data.
print(xmlText)

```

And our output looks like this:
```
<samples>
    <sample>
        <collectionID>testCollectionID</collectionID>
        <title>Test+Title</title>
        <datasetReferenceDate>2020-11-16T15:39:12.2219593-06:00</datasetReferenceDate>
        <abstract>Sample+ID: 0
Accession+Number: C000001
API Number: 1111111111
Sample Type: Rock+Core
Formation: Eagle+Ford
Formation Age: Precambrian</abstract>
        <supplementalInformation>Sample+ID+0+-+Bureau+of+Economic+Geology+Core+Research+Center,+10100+Burnet+Rd.,+Austin,+TX+78758,+512-475-9561</supplementalInformation>
        <dataType>Rock+Core</dataType>
        <coordinates>-98.0,32.0</coordinates>
        <verticalExtent>ft,200.0,120.0</verticalExtent>
    </sample>
    <sample>
        <collectionID>testCollectionID</collectionID>
        <title>Test+Title+2</title>
        <datasetReferenceDate>2020-11-16T15:39:12.2259613-06:00</datasetReferenceDate>
        <abstract>Sample+ID: 1
Accession+Number: C000002
API Number: 2222222222
Sample Type: Rock+Core
Formation: Permian+Basin
Formation Age: Jurassic</abstract>
        <supplementalInformation>Sample+ID+1+-+Bureau+of+Economic+Geology+Core+Research+Center,+10100+Burnet+Rd.,+Austin+TX+78758,+512-475-9561</supplementalInformation>
        <dataType>Rock+Core</dataType>
        <coordinates>-98.0,31.0</coordinates>
        <verticalExtent>ft,250.0,200.0</verticalExtent>
    </sample>
</samples>
```
