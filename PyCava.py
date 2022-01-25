# Tool for generating JNI code

import subprocess
import os
import shutil

import extractStuff
import headerGenerator
import cppGenerator

if (os.path.exists("Cava")):
    shutil.rmtree("Cava")

# Getting filename
filename = "bridge"
#filename = input("File name: ")
#if not os.path.exists(filename + ".java"):
#    print("File does not exist")
#    sys.exit(1)

# Creating Cava folder
if not os.path.exists("Cava"): 
    folder = os.mkdir("Cava")

# Calling javac with -h flag
subprocess.call([os.environ.get("JAVA_HOME") + "/bin/javac.exe", "-d", "./Cava", "-h", "./Cava", filename + ".java"])

os.chdir("Cava")

javaFilename = "bridge.java"
headerFilename = (next(os.walk(os.path.realpath(os.path.curdir)), (None, None, []))[2])[0]

javaContents = extractStuff.javaContents(javaFilename)

headerGenerator.writeToFile(filename, javaContents)
cppGenerator.generate(filename, headerFilename, javaContents)