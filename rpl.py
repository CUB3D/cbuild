#!/usr/bin/python3.4
#usage python3 rpl.py [-ri] <source> <dest> file [outFile]

import sys
import os

sourceString = sys.argv[1]
destinationString = sys.argv[2]
inFileName = sys.argv[3]
outFileName = inFileName

recursive = False
inPlace = False

if "-r" in sys.argv or "-R" in sys.argv:
    sourceString = sys.argv[2]
    destinationString = sys.argv[3]
    inFileName = sys.argv[4]
    recursive = True

if "-i" in sys.argv or "-I" in sys.argv:
    inPlace = True
    sourceString = sys.argv[2]
    destinationString = sys.argv[3]
    inFileName = sys.argv[4]
    outFileName = sys.argv[-1:][0]

print("Replacing string '", sourceString, "' with '", destinationString, "' in file ", inFileName)


def rplSingleFile(inFile, outFile):
    file = open(inFile, "r")
    input = []
    for line in file:
        input.append(line)
    file.close()

    file = open(outFile, "w")
    for line in input:
        if sourceString in line:
            print("[RPL] Match found in file", filePath)
            file.write(line.replace(sourceString, destinationString))
        else:
            file.write(line)
    file.close()

if recursive:
    for path, sub, files in os.walk(inFileName):
        for file in files:
            if not ".o" in file:
                filePath = os.path.join(path, file)
                rplSingleFile(filePath, filePath)
else:
    rplSingleFile(inFileName, outFileName)
