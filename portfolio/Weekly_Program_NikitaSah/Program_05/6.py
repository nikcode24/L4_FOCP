"""
6.	Write a program that takes the name of a file as a command-line argument, 
    and creates a backup copy of that file. The backup should contain an exact 
    copy of the contents of the original and should, obviously, have a different name. 
    Hint: By now, you should be getting the idea that there is a built-in way to do 
    the heavy li ing here! Take a look at the "Brief Tour of the Standard Library" in the docs.
"""

import sys, shutil

if len(sys.argv[1:]) > 0:
    sourceFilename = sys.argv[1:][0]
    DefaultDestinationFilename = "backup-"+sourceFilename
    try:
        destinationFilename = sys.argv[1:][1]
        print("Output FileName Provided")
        shutil.copy(sourceFilename, destinationFilename)
    except:
        print("Output FileName Not Provided")
        shutil.copy(sourceFilename, DefaultDestinationFilename)
else:
    print("Source and Destination Filename Must be Provided.")
    print("python 6.py <Source-FileName> <Destination-Filename>")