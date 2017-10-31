__author__ = 'fordmi'

import os
import time


fileTypes = {

}
timeElapsed = time.time()

rootDir = "C:\\Engineering"

for dirName, subdirList, fileList in os.walk(rootDir):
    print "Found Directory: %s" % dirName
    for fName in fileList:
        print "Found File: %s" % fName
print time.time() - timeElapsed
