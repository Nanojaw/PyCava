# Tool for generating JNI code

import subprocess
import os
import shutil
import sys

import extractStuff
import headerGenerator
import cppGenerator

# Getting filename
filename = input("File name: ")
filename = filename[:filename.find('.')]
if not os.path.isfile(f"./{filename}.java"):
    print("File does not exist")
    sys.exit(1)

# Recreating Cava folder
if (os.path.isdir('./Cava')):
    shutil.rmtree('Cava')
folder = os.mkdir('Cava')
print("Recreated Cava folder")

# Calling javac with -h flag
subprocess.call([os.environ.get("JAVA_HOME") + "/bin/javac.exe", "-d", "./Cava", "-h", "./Cava", filename + ".java"])
print("Called javac with -h flag")

javaFilename = filename + ".java"
headerFilename = (next(os.walk(os.path.realpath(os.path.curdir + "/Cava")), (None, None, []))[2])[0]

javaContents = extractStuff.javaContents(javaFilename)
print(f"Extracted contents of {javaFilename}")

cppGenerator.generateWrapper(filename, headerFilename, javaContents)
print("Generated wrapper file")

headerGenerator.writeToFile(filename, javaContents)
print("Generated header file")

# Generate a cpp file if it doesn't exist
if not os.path.exists(f"{filename}.cpp"):
    cppGenerator.generateCppFile(filename, javaContents)
    print("Generated c++ file")
