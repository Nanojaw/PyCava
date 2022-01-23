# Tool for generating JNI code

import subprocess
import os
import sys

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

