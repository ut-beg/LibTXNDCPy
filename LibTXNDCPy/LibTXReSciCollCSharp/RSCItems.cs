using System;
using System.Collections.Generic;
using System.Formats.Asn1;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using CsvHelper;
using CsvHelper.Configuration;


namespace LibTXReSciCollCSharp {
    public class RSCItems
    {
        private List<RSCItem> _samples;

        public RSCItems()
        {
            _samples = new List<RSCItem>();
        }

        public List<RSCItem> Samples
        {
            get { return _samples; }
        }

        public RSCItem CreateSample()
        {
            RSCItem sample = new RSCItem();
            return sample;
        }

        public void AddItem(RSCItem sample)
        {
            if (!_samples.Contains(sample))
            {
                _samples.Add(sample);
            }
        }

        public void RemoveItem(RSCItem sample)
        {
            if (_samples.Contains(sample))
            {
                _samples.Remove(sample);
            }
        }

        public List<string[]> ToRSCCsvArray()
        {
            List<string[]> ret = new List<string[]>();

            foreach (RSCItem sample in _samples)
            {
                string[] sampX = sample.ToRSCCsvRowArray();
                ret.Add(sampX);
            }

            return ret;
        }

        public void ToRSCCsvFile(string outFilePath)
        {
            List<string[]> rows = ToRSCCsvArray();



            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                ShouldQuote = (field) =>
                {
                    return true;
                }
            };


            using (StreamWriter fileWriter = new StreamWriter(outFilePath, false, Encoding.UTF8))
            using (CsvWriter csvWriter = new CsvWriter(fileWriter, config))
            {
                // Handle the header line
                string[] headers = GetHeaders();
                csvWriter.WriteHeader<RSCItem>();
                csvWriter.NextRecord();

                //Write the business data lines
                csvWriter.WriteRecords(Samples);
            }
        }

        public string ToRSCCsvString()
        {
            StringBuilder ret = new StringBuilder();

            // Assuming you have an equivalent to 'toNDCXml' in C# for XML conversion
            // XmlObject xmlObj = ToNDCXml();
            // Use the xmlObj as needed

            using (StringWriter stringWriter = new StringWriter(ret))
            {
                // Assuming you have an equivalent to 'export' in C# for XML export
                // xmlObj.Export(stringWriter, 0);
            }

            return ret.ToString();
        }

        public string[] GetHeaders()
        {
            string[] ret = {
            "localID",
            "title",
            "alternateTitle",
            "abstract",
            "coordinateLon",
            "coordinateLat",
            "publicationDate",
            "alternateGeometry",
            "onlineResource",
            "browseGraphic",
            "date",
            "verticalExtent",
            "IGSN",
            "parentIGSN",
            "relIGSN",
            "relationType",
            "largerWorkCitation"
        };

            return ret;
        }
    }
}