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

        /// <summary>
        /// Generate the NDC XML for the current set of samples
        /// </summary>
        /// <returns></returns>
        public string toNDCXMLString()
        {
            string ret = null;

            ret = NDCLauncher.launchConvertSamples(this);

            return ret;
        }

        /// <summary>
        /// Export a JSON representation of our set of samples.  This approximates the XML format, but it's in JSON.  This can be used as the input to NDCconvertSamples.py
        /// </summary>
        /// <returns></returns>
        public string toJson()
        {
            string ret = null;

            ret = NDCLauncher.toJson(this, false);

            return ret;
        }

        /// <summary>
        /// Exports a json-serialized representation of our set of samples which is then URLEncoded.  This can be used as the input to NDCconvertSamples.py
        /// </summary>
        /// <returns></returns>
        public string toUrlEncodedJson()
        {
            string ret = null;

            ret = NDCLauncher.toJson(this, true);

            return ret;
        }
    }
}
