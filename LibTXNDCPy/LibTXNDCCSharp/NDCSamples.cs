using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXNDCCSharp
{
    /// <summary>
    /// Represents a collection of samples to be serialized
    /// </summary>
    public class NDCSamples
    {
        public List<NDCSample> samples
        {
            get;
            set;
        } = new List<NDCSample>();

        public string toNDCXMLString()
        {
            string ret = null;

            ret = NDCLauncher.launchConvertSamples(this);

            return ret;
        }
    }
}
