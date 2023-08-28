# NDCconvertSamples.py - Aaron Averett - Bureau of Economic Geology, 2020
# This serves as the entry point for consuming LibTXNDCPy from a command line without the need to write Python code of your own.
# This can also be used to access LibTXNDCPy from other applications, even if they don't support launching Python natively.

import NDCSamples
from NDCSampleFactory import NDCSampleFactory
import sys
from urllib.parse import unquote
from urllib.parse import quote
import argparse

class NDCSampleConverter:

    def __init__(self, testmode=False):

        #Initialize some class vars
        self.json = ""
        self.samples = None
        self.inFilePath = None
        self.urlEncodedJson = None
        self.outFilePath = None
        self.doUrlEncode = False
        self.xml = None

        if testmode != True:
            self.parseArgs()

    def parseArgs(self):
        #Set up parsing of the command line arguments
        parser = argparse.ArgumentParser("NDCconvertSamples")

        parser.add_argument("-f", required=False, help="load data from file")
        parser.add_argument("-d", required=False, help="URLEncoded json data")
        parser.add_argument("-o", required=False, help="Output file path.  If this is empty, we output to the console.")
        parser.add_argument("-u", action="store_true", help="URLEncode the output")

        parsedargs = parser.parse_args()

        #go from parsed arguments to set up class vars
        if(parsedargs.f != None):
            self.inFilePath = parsedargs.f

        if(parsedargs.d != None):
            self.urlEncodedJson = parsedargs.d

        if(parsedargs.o != None):
            self.outFilePath = parsedargs.o

        if(parsedargs.u != None):
            self.doUrlEncode = parsedargs.u
            
    def loadFromUrlEncodedString(self,blob):
        #De-urlencode the char data into some json (a slightly less big fat blob of char data)
        self.json = unquote(blob)

    def loadFromFile(self, filename):
        with open(filename) as reader:
            self.json = reader.read()

    def populateSamples(self):
        if self.json != "":
            fac = NDCSampleFactory()

            #Hand the json off to our library and get an NDCSample back
            self.samples = fac.createSamplesWithJson(self.json)

    def outToConsole(self, data):
        print(data)

    def outToFile(self, data):
        outfilename = self.parsedargs.o
        with open(outfilename, "w") as writer:
            writer.write(data)

    def doRequestedAction(self):
        #option D 
        if(self.urlEncodedJson != None):
            self.loadFromUrlEncodedString(self.urlEncodedJson)

        #option F
        elif(self.inFilePath != None):
           self.loadFromFile(self.inFilePath)

        #populate our samples object
        self.populateSamples()

        #Export the NDCSample to its XML expression
        self.xml = self.samples.toNDCXmlString()

        #if the user requested that we urlencode the output, do so.
        if(self.xml != None and self.doUrlEncode == True):
            xml = quote(self.xml)

        if(self.outFilePath != None):
            self.outToFile(self.xml)
        else: 
            #Output the string to the console
            self.outToConsole(self.xml)


if __name__ == '__main__':
    app = NDCSampleConverter()
    app.doRequestedAction()
