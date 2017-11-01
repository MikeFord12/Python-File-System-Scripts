__author__ = 'fordmi'

import os
import time


fileTypes = {

}
userPath = raw_input("Enter in desired file path: ")

timeElapsed = time.time()

for dirName, subdirList, fileList in os.walk(userPath):
    if '.svn' in subdirList:
        subdirList.remove('.svn')
    for fName in fileList:
        extension = os.path.splitext(fName)[1].lower()
        if extension in fileTypes:
            fileTypes[extension] += 1
        elif extension == "":
            fileTypes[fName] = 1
        else:
            fileTypes[extension] = 1

logFile = open("log.txt","w")


for elements in fileTypes:
    logFile.write("%s: %d\n" % (elements, fileTypes[elements]))
logFile.write("Time Elapsed: %.2fs" % (time.time() - timeElapsed))
