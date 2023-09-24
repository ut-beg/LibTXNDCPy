using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXReSciCollCSharp
{
    /// <summary>
    /// Represents a sample of some kind from an oil or gas well.  While not declared as an abstract class, this class is really meant to be extended.
    /// </summary>
    public class RSCSample : RSCItem
    {
        /// <summary>
        /// A description of the type of sample, such as a rock core, cuttings, thin section, etc.
        /// </summary>
        public string? SampleType { get; set; }

        protected override List<string> ComposeAbstractElements()
        {
            List<string> elements = base.ComposeAbstractElements();

            if (SampleType != null)
            {
                AddAbstractElement(SampleType, "Sample Type", elements);
            }

            return elements;
        }
    }
}
