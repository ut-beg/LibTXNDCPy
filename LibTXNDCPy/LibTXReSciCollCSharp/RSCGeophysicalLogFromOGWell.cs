using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXReSciCollCSharp
{
    /// <summary>
    /// Represents a geophysical log
    /// </summary>
    public class RSCGeophysicalLogFromOGWell : RSCSampleFromOGWell
    {
        public RSCGeophysicalLogFromOGWell() {
            DataType = "Well logs";
        }
    }
}
