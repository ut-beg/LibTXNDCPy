from NDCRockCoreSample import NDCRockCoreSample

testfilePath = '../../Auxiliary/NDC_XML_file_example.xml'
outfilePath = '../../Auxiliary/testout.xml'

rcs = NDCRockCoreSample()

rcs.apiNumber = "1111111111"
rcs.internalReferenceNumber1Description = "Sample ID"
rcs.internalReferenceNumber1 = "0"
rcs.internalReferenceNumber2Description = "Accession Number"
rcs.internalReferenceNumber2 = "C000001"
rcs.formationName = "Eagle Ford"

print(rcs.abstract)
