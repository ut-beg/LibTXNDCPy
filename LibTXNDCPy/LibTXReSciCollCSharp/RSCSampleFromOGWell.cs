using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibTXReSciCollCSharp
{
    /// <summary>
    /// Represents a sample that comes from an oil and gas well.  This class is meant to be an intermediate class that you'd extend with some other type, such as a core, or cuttings.
    /// </summary>
    public class RSCSampleFromOGWell : RSCSample
    {
        /// <summary>
        /// The API number for the oilwell that this sample is derived from
        /// </summary>
        public string? ApiNumber { get; set; }

        /// <summary>
        /// The lease name of the oil or gas well that this sample is drived from
        /// </summary>
        public string? LeaseName { get; set; }

        /// <summary>
        /// Well number of the oil or gas well that this sample is derived from.
        /// </summary>
        public string? WellNumber { get; set; }

        /// <summary>
        /// The name of the state/province/other administrative division where the well is located.
        /// </summary>
        public string? StateName { get; set; }

        /// <summary>
        /// The name of the county/parish where the well is located.
        /// </summary>
        public string? CountyName { get; set; }

        /// <summary>
        /// The name of the country where the well is located.
        /// </summary>
        public string? CountryName { get; set; }

        /// <summary>
        /// The name of the field where the well is located.
        /// </summary>
        public string? FieldName { get; set; }

        /// <summary>
        /// The name of the operator of the well
        /// </summary>
        public string OperatorName { get; set; }

        public RSCSampleFromOGWell() { }

        protected override List<string> ComposeAbstractElements()
        {

            List<string> elements = base.ComposeAbstractElements();

            if (ApiNumber != null)
            {
                AddAbstractElement(ApiNumber, "API Number", elements);
            }

            if(LeaseName != null)
            {
                AddAbstractElement(LeaseName, "Lease Name", elements);
            }

            if(WellNumber != null)
            {
                AddAbstractElement(WellNumber, "Well Number", elements);
            }

            if(StateName != null)
            {
                AddAbstractElement(StateName, "State Name", elements);
            }

            if(CountyName != null)
            {
                AddAbstractElement(CountyName, "CountyName", elements);
            }

            if(CountryName != null)
            {
                AddAbstractElement(CountryName, "Country Name", elements);
            }

            if (FieldName != null)
            {
                AddAbstractElement(FieldName, "Field Name", elements);
            }

            if (OperatorName != null)
            {
                AddAbstractElement(OperatorName, "Operator Name", elements);
            }

            return elements;
        }
    }
}
