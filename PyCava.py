# Tool for generating JNI code

import subprocess
import os
import sys

filename = input("File name: ")
if not os.path.exists(filename + ".java"):
    print("File does not exist")
    sys.exit(1)

if not os.path.exists("Cava"): 
    folder = os.mkdir("Cava")

subprocess.call([os.environ.get("JAVA_HOME") + "/bin/javac.exe", "-d", "./Cava", "-h", "./Cava", filename + ".java"])