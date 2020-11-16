using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
 *  This is an example for consuming LibTXNDCPy from C#.
 */

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Create a "samples" container object.
            LibTXNDCCSharp.NDCSamples samples = new LibTXNDCCSharp.NDCSamples();


            //Create sample object 
            LibTXNDCCSharp.NDCRockCoreSample rcs1 = new LibTXNDCCSharp.NDCRockCoreSample();

            //Set the values on the sample object.  In practice, you'd fill this out from your database or wherever your data actually live.  Here, for testing purposes, we'll just fill them in with constant values.
            rcs1.collectionID = "testCollectionID";
            rcs1.title = "Test Title";
            rcs1.coordinatesLatitude = 32.0;
            rcs1.coordinatesLongitude = -98.0;
            rcs1.supplementalInformation = "Sample ID 0 - Bureau of Economic Geology Core Research Center, 10100 Burnet Rd., Austin, TX 78758, 512-475-9561";
            rcs1.datasetReferenceDate = DateTime.Now;
            rcs1.dataType = "Rock Core";
            rcs1.apiNumber = "1111111111";
            rcs1.internalReferenceNumber1Description = "Sample ID";
            rcs1.internalReferenceNumber1 = "0";
            rcs1.internalReferenceNumber2Description = "Accession Number";
            rcs1.internalReferenceNumber2 = "C000001";
            rcs1.formationName = "Eagle Ford";
            rcs1.formationAge = "Precambrian";
            rcs1.verticalExtentTop = 120;
            rcs1.verticalExtentBottom = 200;
            rcs1.verticalExtentUnit = "ft";
            rcs1.sampleTypeDesc = "Rock Core";

            //Create a second object.
            LibTXNDCCSharp.NDCRockCoreSample rcs2 = new LibTXNDCCSharp.NDCRockCoreSample();
            rcs2.collectionID = "testCollectionID";
            rcs2.title = "Test Title 2";
            rcs2.coordinatesLatitude = 31.0;
            rcs2.coordinatesLongitude = -98.0;
            rcs2.supplementalInformation = "Sample ID 1 - Bureau of Economic Geology Core Research Center, 10100 Burnet Rd., Austin TX 78758, 512-475-9561";
            rcs2.datasetReferenceDate = DateTime.Now;
            rcs2.dataType = "Rock Core";
            rcs2.apiNumber = "2222222222";
            rcs2.internalReferenceNumber1Description = "Sample ID";
            rcs2.internalReferenceNumber1 = "1";
            rcs2.internalReferenceNumber2Description = "Accession Number";
            rcs2.internalReferenceNumber2 = "C000002";
            rcs2.formationName = "Permian Basin";
            rcs2.formationAge = "Jurassic";
            rcs2.verticalExtentTop = 200;
            rcs2.verticalExtentBottom = 250;
            rcs2.verticalExtentUnit = "ft";
            rcs2.sampleTypeDesc = "Rock Core";

            //Add the samples our samples collection
            samples.samples.Add(rcs1);
            samples.samples.Add(rcs2);

            //Now, we can ask the samples object to run the underlying Python program to do the conversion and capture the console output from it.
            string sampleXml = samples.toNDCXMLString();

            //Write the XML to the console.  You'd presumably save this to a file or write it into the HTTP response or something in a real application.
            Console.WriteLine(sampleXml);

            //When run from the Visual Studio debugger, the command line window disappears, so we'll 
            Console.WriteLine("Press enter to quit.");
            Console.ReadLine();
        }
    }
}
