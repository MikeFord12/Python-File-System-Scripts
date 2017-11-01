__author__ = 'fordmi'

import os

matchingFiles = []
paths = []
printFileFlag = True
rootFilePath = raw_input("Type starting directory for search. Enter to skip (default will be current directory): ")

if not len(rootFilePath):
    rootFilePath = "C:"
while not os.path.isdir(rootFilePath):
    print("Directory entered is not valid.")
    rootFilePath = raw_input("Type starting directory for search. Enter to skip (default will be current directory).")

filesToFind = raw_input("Type in file search criteria: ")

for dirName, subdirList, fileList in os.walk(rootFilePath):
    for file in fileList:
        if filesToFind in file:
            paths.append(os.path.join(dirName,file))
            matchingFiles.append(file)

if not len(matchingFiles):
    print("No matching files found.")
else:
    for index in range(1,len(matchingFiles)):
        print "%d. %s" % (index, matchingFiles[index-1])

    fileChoice = input("Enter in file number from list below to search: ")

    while not fileChoice > -1 and not fileChoice <= len(matchingFiles):
            fileChoice = input("Number not valid. Must be betwwen %d and %d.\n "
                               "Enter file number from file list to search: " % (0, len(matchingFiles)))

    searchString = raw_input("Enter in text to search for: ")
    while not len(searchString) > 0:
        searchString = raw_input("Enter in text to search for: ")

    if fileChoice ==0:
        for index in range(1,len(matchingFiles)):
            with open(paths[index-1]) as f:

                for lineNumber, line in enumerate(f):
                    if searchString in line:
                        if printFileFlag:
                            print("File: %s" % paths[index-1])
                            printFileFlag = False
                        print "%d. %s" % (lineNumber, line)
                    printFileFlag = True

    else:
        with open(os.path.join(rootFilePath,matchingFiles[fileChoice-1])) as f:
            for lineNumber, line in enumerate(f):
                if searchString in line:
                    if printFileFlag:
                        print("File: %s" % paths[fileChoice-1])
                        printFileFlag = False
                    print "%d. %s" % (lineNumber, line)
                printFileFlag = True

raw_input("Press enter to exit.")






