# NDCconvertSamples.py - Aaron Averett - Bureau of Economic Geology, 2020
# This serves as the entry point for consuming LibTXNDCPy from a command line without the need to write Python code of your own.
# This can also be used to access LibTXNDCPy from other applications, even if they don't support launching Python natively.

import NDCSamples
from NDCSampleFactory import NDCSampleFactory
import sys
from urllib.parse import unquote
from urllib.parse import quote
import argparse

#Set up parsing of the command line arguments

parser = argparse.ArgumentParser("NDCconvertSamples")

parser.add_argument("-f", required=False, help="load data from file")
parser.add_argument("-d", required=False, help="URLEncoded json data")
parser.add_argument("-o", required=False, help="Output file path.  If this is empty, we output to the console.")
parser.add_argument("-u", action="store_true", help="URLEncode the output")

parsedargs = parser.parse_args()

json = ""

#option D 
if(parsedargs.d != None):
    #Got the data from the command line
    encodedjson = parsedargs.d
    #De-urlencode the char data into some json (a slightly less big fat blob of char data)
    json = unquote(encodedjson)

#option F
elif(parsedargs.f != None):
    filename = parsedargs.f
    with open(filename) as reader:
        json = reader.read()

fac = NDCSampleFactory()

#Hand the json off to our library and get an NDCSample back
samples = fac.createSamplesWithJson(json)

#Export the NDCSample to its XML expression
xml = samples.toNDCXmlString()

#if the user requested that we urlencode the output, do so.
if(parsedargs.u != None and parsedargs.u == True):
    xml = quote(xml)

if(parsedargs.o != None):
    outfilename = parsedargs.o
    with open(outfilename, "w") as writer:
        writer.write(xml)
else: 
    #Output the string to the console
    print(xml)