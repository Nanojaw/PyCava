def writeToFile(filename, jC):
    realHeader = open(f"{filename}.h", "w")

    linesString = "#pragma once\n"

    indentation = ""

    for package in jC.packages:
        linesString += indentation + "namespace " + package + "\n" + indentation + "{\n"
        indentation += "    "

    linesString += indentation + "class " + jC.classs + "\n"
    linesString += indentation + "{\n"

    indentation += "    "

    for method in jC.methods:
        firstParenthesis = method.find("(")
        secondParenthesis = method.find(")")

        if (firstParenthesis + 1 != secondParenthesis):
            method = method.replace("String", "std::wstring")

            method = method.replace("byte", "char")
            method = method.replace("long", "long long")
            method = method.replace("char", "wchar_t")
            method = method.replace("bolean", "bool")

        linesString += indentation + method + "\n"

    realHeader.write(linesString)