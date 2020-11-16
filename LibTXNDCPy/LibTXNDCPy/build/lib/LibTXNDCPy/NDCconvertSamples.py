# NDCconvertSamples.py - Aaron Averett - Bureau of Economic Geology, 2020
# This serves as the entry point for consuming LibTXNDCPy from a command line without the need to write Python code of your own.
# This can also be used to access LibTXNDCPy from other applications, even if they don't support launching Python natively.

import NDCSamples
from NDCSampleFactory import NDCSampleFactory
import sys
from urllib.parse import unquote

#This script expects a single argument, which is an urlencoded string containing the JSON version of our object.

#Grab our urlencoded string - big fat blob of char data
encodedjson = sys.argv[1]

fac = NDCSampleFactory()

#De-urlencode the char data into some json (a slightly less big fat blob of char data)
json = unquote(encodedjson)

#Hand the json off to our library and get an NDCSample back
samples = fac.createSamplesWithJson(json)

#Export the NDCSample to its XML expression
xml = samples.toNDCXmlString()

#Output the string to the console
print(xml)