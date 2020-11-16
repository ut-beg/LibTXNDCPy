using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXNDCCSharp
{
    public class NDCSampleFromOGWell: NDCSample
    {
        public string apiNumber = null;

        public string leaseName = null;

        public string wellNumber = null;

        public string stateName = null;

        public string countyName = null;

        public string countryName = null;

        public string fieldName = null;

        public string operatorName = null;

        public NDCSampleFromOGWell()
        {
            classKey = "SampleFromOGWell";
        }
    }
}
