
using LibTXReSciCollCSharp;
using System.Security.Cryptography;
using System;

//Use the rock core sample
RSCSample s = new RSCSample();

s.LocalID = "11111";
s.Title = "Test Title";
s.AlternateTitle = "Test Alternate title";
s.DataType = "Test data type";
s.CoordinatesLatitude = 32.0;
s.CoordinatesLongitude = -95.0;
s.PublicationDate = DateTime.Now;
s.AlternateGeometry = "Test alternate geometry";
s.OnlineResource = "https://www.beg.utexas.edu";
s.BrowseGraphic = "https://www.beg.utexas.edu";
s.Date = new DateTime(2023, 1, 1);
s.VerticalExtentBottom = 1200;
s.VerticalExtentTop = 800;
s.VerticalExtentUnit = "ft";
s.Igsn = "00000001";
s.ParentIgsn = "00000000";
s.RelIgsn = "00000002";
s.RelationType = "Beans";
s.LargerWorkCitation = "Larger work citation test value";

s.SampleType = "Cuttings";

RSCItems rss = new RSCItems();
rss.AddItem(s);

rss.ToRSCCsvFile("testoutput.csv");