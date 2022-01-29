import extractStuff
import converter

import os

def generateWrapper(filename: str, hFilename: str, content):
    lineString = f"#include <string>\n#include <{filename}.h>\n#include <{hFilename}>\n"

    #  Adding all of the functions to be wrapped
    for i in range(len(content.methods)):

        # Adding definition to functions in header file
        defFunc = content.methods[i][:content.methods[i].find(' ') + 1] + "Java_"
        for pack in content.packages:
            defFunc += pack + "_"
        defFunc += content.classs + "_" + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        hFile = open(hFilename)
        hLines = hFile.readlines()
        defFunc = defFunc[defFunc.find(" "):]
        # Adding parameters to definition
        params = extractStuff.getMethodParams(content.methods[i])

        defFunc += " (JNIEnv* env, jobject obj"
        for j in range(len(params)):
            defFunc += f", {converter.CppToJNI[params[j]]} v{str(j)}"
        defFunc += ")\n"

        # Getting cpp function
        cppFunc = ""
        for pack in content.packages:
            cppFunc += pack + "."
        cppFunc += content.classs + "." + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to cpp function

        reference = "" # Reference and release is for handling reference objects that require cleanup
        release = ""

        cppFunc += "("
        for j in range(len(params)):
            if params[j] == "std::wstring": 
                reference += f"    const wchar_t* r{str(j)} = (*env)->GetStringChars(env, v{str(j)}, nullptr);\n"
                cppFunc += f", std::wstring(r{str(j)})"
                release += f"    (*env)->ReleaseStringChars(env, v{str(j)}, r{str(j)});\n"
            else:
                cppFunc += f", ({params[j]}) v{str(j)}"
        cppFunc += ");\n"
        if cppFunc.find(",") != -1: cppFunc = cppFunc[:cppFunc.find(",")] + cppFunc[cppFunc.find(",") + 2:]

        lineString += (
        "\n" + 
        defFunc + 
        "{\n" +
        reference +
        "    auto result = " + cppFunc +
        release +
        "    return result;\n"
        "}\n"
        )

    file = open(hFilename +  ".cpp", 'w')
    file.write(lineString)
    file.close()

def generateCppFile(filename: str, content):
    cppFile = open(f"../{filename}.cpp", 'w')
