using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXNDCCSharp
{
    public class NDCRockCoreSample : NDCSampleFromOGWell
    {
        public string sampleTypeDesc = null;
        public string formationName = null;
        public string formationAge = null;

        public NDCRockCoreSample()
        {
            classKey = "RockCoreSample";
        }
    }
}
