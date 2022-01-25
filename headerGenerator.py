def writeToFile(filename, jC):
    realHeader = open(f"{filename}.h", "w")

    linesString = "#pragma once\n\n#include <string>\n\n"

    indentation = ""

    for package in jC.packages:
        linesString += indentation + "namespace " + package + "\n" + indentation + "{\n"
        indentation += "    "

    linesString += indentation + "class " + jC.classs + "\n"
    linesString += indentation + "{\n"

    indentation += "    "

    for method in jC.methods:
        linesString += indentation + method + "\n"

    indentation = indentation[:len(indentation) -4]

    linesString += indentation + "};\n"

    for i in range(int(len(indentation)/4)):
        indentation = indentation[:len(indentation) -4]
        linesString += indentation + "}\n"

    realHeader.write(linesString)