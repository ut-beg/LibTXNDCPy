using System;
using System.Collections.Generic;
using System.IO;
using System.Linq.Expressions;

using CsvHelper;
using CsvHelper.Configuration.Attributes;
using static System.Collections.Specialized.BitVector32;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace LibTXReSciCollCSharp {
    public class RSCItem
    {
        // Private fields
        private string _localID;
        private double? _coordinatesLatitude;
        private double? _coordinatesLongitude;
        private string _title;
        private string _alternateTitle;
        private string _abstract;
        private string _dataType;
        private DateTime? _publicationDate;
        private string _collectionID;
        private string _alternateGeometry;
        private string _onlineResource;
        private string _browseGraphic;
        private DateTime? _date = DateTime.Now;
        private string _verticalExtent;
        private double? _verticalExtentTop;
        private double? _verticalExtentBottom;
        private string _verticalExtentUnit;
        private string _igsn;
        private string _parentIgsn;
        private string _relIgsn;
        private string _relationType;
        private string _largerWorkCitation;
        private string _internalReferenceNumber1;
        private string _internalReferenceNumber2;
        private string _internalReferenceNumber1Description;
        private string _internalReferenceNumber2Description;
        private string _supplementalInformation;
        private string _repositoryPhoneNumber;
        private string _repositoryEmailAddress;
        private string _repositoryName;
        private string _repositoryPhysicalAddress;
        private string _repositoryMailingAddress;
        private string _supplementalInformationAdditional;
        private string _abstractMore;

        private string _attachmentFileName;

        // Public properties

        /// <summary>
        /// Identifier provided by the collection owner for uniquely identifying this item, such as a well API, database primary key, et cetera.
        /// </summary>
        [Name("localID")]
        [Index(0)]
        public string LocalID
        {
            get { return _localID; }
            set { _localID = value; }
        }

        /// <summary>
        /// Latitude in WGS84, presumably of the site where the sample was collected.
        /// </summary>
        [Name("coordinateLat")]
        [Index(6)]
        public double? CoordinatesLatitude
        {
            get { return _coordinatesLatitude; }
            set { _coordinatesLatitude = value; }
        }


        /// <summary>
        /// Longitude in WGS84, presumably of the site where the sample was collected.
        /// </summary>
        [Name("coordinateLon")]
        [Index(5)]
        public double? CoordinatesLongitude
        {
            get { return _coordinatesLongitude; }
            set { _coordinatesLongitude = value; }
        }

        /// <summary>
        /// The primary title for this item.
        /// </summary>
        [Name("title")]
        [Index(1)]
        public string Title
        {
            get { return _title; }
            set { _title = value; }
        }

        /// <summary>
        /// Collection owners may elect to provide an alternate tite
        /// </summary>
        [Name("alternateTitle")]
        [Index(2)]
        public string AlternateTitle
        {
            get { return _alternateTitle; }
            set { _alternateTitle = value; }
        }

        /// <summary>
        /// Main description of the item.  This should be human readable and can contain anything you want.
        /// </summary>
        [Name("abstract")]
        [Index(3)]
        public string Abstract
        {
            get
            {
                if (!string.IsNullOrEmpty(_abstract))
                    return _abstract;
                else
                    return ComposeAbstract();
            }
            set { _abstract = value; }
        }

        /// <summary>
        /// A controlled vocabulary of data types.  This should come from the controlled vocabulary listed here:
        /// https://www.sciencebase.gov/vocab/categories?parentId=4f4e475ee4b07f02db47df22
        /// </summary>
        [Name("dataType")]
        [Index(4)]
        public string DataType
        {
            get { return _dataType; }
            set { _dataType = value; }
        }

        /// <summary>
        /// String representation of the publication date of the metadata.  Defaults to current date (because we're generating our metadata... today.)
        /// </summary>
        [Name("publicationDate")]
        [Index(7)]
        public string sPublicationDate
        {
            get
            {
                string ret = string.Empty;

                if (this.Date.HasValue)
                {
                    ret = this.Date.Value.ToString("yyyyMMdd");
                }
                
                return ret;
            }
        }

        /// <summary>
        /// Publication date of the metadata.  This is where you should set this, if you're not going to just rely on the default, which is today.
        /// </summary>
        [Ignore]
        public DateTime? PublicationDate
        {
            get { return _publicationDate; }
            set { _publicationDate = value; }
        }

        /// <summary>
        /// Alternate geometry of some other type.
        /// </summary>
        [Name("alternateGeometry")]
        [Index(8)]
        public string AlternateGeometry
        {
            get { return _alternateGeometry; }
            set { _alternateGeometry = value; }
        }

        /// <summary>
        /// URL to an online resource related to this sample.
        /// </summary>
        [Name("onlineResource")]
        [Index(9)]
        public string OnlineResource
        {
            get { return _onlineResource; }
            set { _onlineResource = value; }
        }

        /// <summary>
        /// URL for the browse graphic
        /// </summary>
        [Name("browseGraphic")]
        [Index(10)]
        public string BrowseGraphic
        {
            get { return _browseGraphic; }
            set { _browseGraphic = value; }
        }

        /// <summary>
        /// String representation of the date for use in the CSV.  Read-only.
        /// </summary>
        [Name("date")]
        [Index(11)]
        public string sDate
        {
            get
            {
                string ret = string.Empty;

                if(this.Date.HasValue)
                {
                    ret = this.Date.Value.ToString("yyyyMMdd");
                }

                return ret;
            }
        }

        /// <summary>
        /// Meaningful date associated with this item, such as when it was collected.
        /// </summary>
        [Ignore]
        public DateTime? Date
        {
            get { return _date; }
            set { _date = value; }
        }

        /// <summary>
        /// String value of the vertical extent for use in the csv output.  Ex: "ft,200,400"
        /// </summary>
        [Name("verticalExtent")]
        [Index(12)]
        public string VerticalExtent
        {
            get { return _verticalExtent; }
            set { _verticalExtent = value; }
        }

        /// <summary>
        /// The top of the vertical extent, in whatever units are specified.
        /// </summary>
        [Ignore]
        public double? VerticalExtentTop
        {
            get { return _verticalExtentTop; }
            set
            {
                _verticalExtentTop = value;
                UpdateVerticalExtent();
            }
        }

        /// <summary>
        /// The bottom of the vertical extent, in whatever units are specified.
        /// </summary>
        [Ignore]
        public double? VerticalExtentBottom
        {
            get { return _verticalExtentBottom; }
            set
            {
                _verticalExtentBottom = value;
                UpdateVerticalExtent();
            }
        }

        /// <summary>
        /// Units used in the vertical extent.  Must be "ft" or "m"
        /// </summary>
        [Ignore]
        public string VerticalExtentUnit
        {
            get { return _verticalExtentUnit; }
            set
            {
                if (value != null && value != "m" && value != "ft")
                {
                    throw new ArgumentException("Invalid vertical extent unit.");
                }
                _verticalExtentUnit = value;
                UpdateVerticalExtent();
            }
        }

        /// <summary>
        /// IGSN of this sample
        /// </summary>
        [Name("IGSN")]
        [Index(13)]
        public string Igsn
        {
            get { return _igsn; }
            set { _igsn = value; }
        }

        /// <summary>
        /// IGSN of the parent sample, if this one is derived from another.
        /// </summary>
        [Name("parentIGSN")]
        [Index(14)]
        public string ParentIgsn
        {
            get { return _parentIgsn; }
            set { _parentIgsn = value; }
        }

        /// <summary>
        /// IGSN of a related sample or subsample.  Only the IGSN is required, not the full address.
        /// </summary>
        [Name("relIGSN")]
        [Index(15)]
        public string RelIgsn
        {
            get { return _relIgsn; }
            set { _relIgsn = value; }
        }

        /// <summary>
        /// Relationship of the IGSN to the largerWorkCitation.  Use the DataCite type vocabulary here:
        /// https://www.sciencebase.gov/vocab/vocabulary/611d428bbfff3461918aba6e
        /// </summary>
        [Name("relationType")]
        [Index(16)]
        public string RelationType
        {
            get { return _relationType; }
            set { _relationType = value; }
        }

        /// <summary>
        /// Physical sample connection to publication (DOI). The collection may document a larger
        /// set of samples with only a section used in a journal article.Only the DOI itself is
        /// required, not the full web link.
        /// </summary>
        [Name("largerWorkCitation")]
        [Index(17)]
        public string LargerWorkCitation
        {
            get { return _largerWorkCitation; }
            set { _largerWorkCitation = value; }
        }

        /// <summary>
        /// Full name of file that is to be linked to the item via the file attachment process. A full folder/directory path is not required, just the filename and extension.Must match the name used during file attachment ingest
        /// </summary>
        [Name("attachmentFileName")]
        [Index(18)]
        public string AttachmentFileName
        {
            get {
                return _attachmentFileName;
            }

            set { 
                _attachmentFileName = value; 
            }
        }

        // Constructor
        public RSCItem()
        {
            // Initialize fields here if needed
        }

        /// <summary>
        /// Method to add an element and label to the set of items to be included in the abstract text
        /// </summary>
        /// <param name="element">The value to be shown to the user.</param>
        /// <param name="label">The name of the element, to be shown as the label in the list.</param>
        /// <param name="list">The list of properties to add to</param>
        public virtual void AddAbstractElement(string element, string label, List<string> list)
        {
            if (!string.IsNullOrEmpty(element) && !string.IsNullOrEmpty(label))
            {
                list.Add(label + ": " + element);
            }
        }

        /// <summary>
        /// Composes the list of abstract elements.
        /// </summary>
        /// <returns>List of strings, each one meant to be a line in the "abstract" value.</returns>
        protected virtual List<string> ComposeAbstractElements()
        {
            var ret = new List<string>();

            return ret;
        }

        /// <summary>
        /// Composes the value for the "abstract" field, which is basically a longtext that can contain whatever you want.
        /// </summary>
        /// <returns></returns>
        protected virtual string ComposeAbstract()
        {
            string ret = "";

            // Build the list 
            var elementList = ComposeAbstractElements();

            ret = string.Join("\r\n", elementList);

            return ret;
        }

        // Method to validate for CSV export
        private void ValidateForCsv()
        {
            // Make sure we have a title
            if (string.IsNullOrEmpty(_title))
            {
                throw new ArgumentException("Title is required and cannot be empty.");
            }

            // Make sure we have an abstract value
            if (string.IsNullOrEmpty(_abstract) && ComposeAbstract() == string.Empty)
            {
                throw new ArgumentException("Abstract is required and cannot be empty.");
            }

            // Validate dataset reference date field
            if (_publicationDate == null)
            {
                throw new ArgumentException("Dataset reference date is required and cannot be empty.");
            }
        }

        // Method to update the vertical extent property
        private void UpdateVerticalExtent()
        {
            if (!string.IsNullOrEmpty(_verticalExtentUnit) && _verticalExtentTop != null && _verticalExtentBottom != null)
            {
                _verticalExtent = $"{_verticalExtentUnit},{_verticalExtentBottom},{_verticalExtentTop}";
            }
            else
            {
                _verticalExtent = null;
            }
        }

        private void AddSupplementalInformationElement(string element, string label, List<string> list)
        {
            if(element != null && label != null)
            {
                list.Add(label + ": " + element);
            }
        }

        private List<string> ComposeSupplementalInformationElements()
        {
            List<string> ret = new List<string>();

            AddSupplementalInformationElement(_repositoryName, "Repository Name", ret);
            AddSupplementalInformationElement(_repositoryEmailAddress, "Repository Email Address", ret);
            AddSupplementalInformationElement(_repositoryPhoneNumber, "Repository Phone Number", ret);
            AddSupplementalInformationElement(_repositoryMailingAddress, "Repository Mailing Address", ret);
            AddSupplementalInformationElement(_repositoryPhysicalAddress, "Repository Physical Address", ret);
            AddSupplementalInformationElement(_supplementalInformationAdditional, "Additional Information", ret);

            return ret;
        }

        private string ComposeSupplementalInformation()
        {
            List<string> elementList = ComposeSupplementalInformationElements();

            return string.Join("\r\n", elementList);
        }

        // Method to convert the object to an array for CSV export
        public string[] ToRSCCsvRowArray()
        {
            // Validate and make sure we have all the required fields
            ValidateForCsv();

            List<string> parts = new List<string>();

            parts.Add(_localID);
            parts.Add(_title);
            parts.Add(_alternateTitle);
            parts.Add(_abstract);
            parts.Add(_coordinatesLongitude?.ToString());
            parts.Add(_coordinatesLatitude?.ToString());

            if (_publicationDate != null)
            {
                parts.Add(_publicationDate.Value.ToString("yyyyMMdd"));
            }
            else
            {
                parts.Add(null);
            }

            parts.Add(_alternateGeometry);
            parts.Add(_onlineResource);
            parts.Add(_browseGraphic);

            if (_date != null)
            {
                parts.Add(_date.Value.ToString("yyyyMMdd"));
            }
            else
            {
                parts.Add(null);
            }

            parts.Add(_verticalExtent);
            parts.Add(_igsn);
            parts.Add(_parentIgsn);
            parts.Add(_relIgsn);
            parts.Add(_relationType);
            parts.Add(_largerWorkCitation);

            return parts.ToArray();
        }
    }
}