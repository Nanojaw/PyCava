def writeToFile(filename: str, jC):
    realHeader = open(f"Cava/{filename}.h", "w")

    linesString = "#pragma once\n\n#include <string>\n#include <vector>\n\n"

    indentation = ""

    for package in jC.packages:
        linesString += f"{indentation}namespace {package}\n{indentation}" + "{\n"
        indentation += "    "

    linesString += indentation + f"class {jC.classs}\n"
    linesString += indentation + "{\n" 
    linesString += indentation + "public:\n"

    indentation += "    "

    for method in jC.methods:
        linesString += f"{indentation}static {method}\n"

    indentation = indentation[:len(indentation) -4]

    linesString += indentation + "};\n"

    for i in range(int(len(indentation)/4)):
        indentation = indentation[:len(indentation) -4]
        linesString += indentation + "}\n"

    realHeader.write(linesString)