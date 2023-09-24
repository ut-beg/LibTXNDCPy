using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXReSciCollCSharp
{
    /// <summary>
    /// Represents a rock core that came out of an oil and gas well.
    /// </summary>
    public class RSCRockCoreFromOGWell : RSCSampleFromOGWell
    {
        public RSCRockCoreFromOGWell() 
        {
            DataType = "Rock cores";
        }
    }
}
