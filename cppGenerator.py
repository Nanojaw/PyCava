import extractStuff

def generate (filename, hFilename, content):
    lineString = f"#include <string>\n#include <{filename}.h>\n#include <{hFilename}>\n"

    #  Adding all of the functions to be wrapped
    for i in range(len(content.methods)):

        # Adding definition to functions in header file
        defFunc = content.methods[i][:content.methods[i].find(' ') + 1] + "Java_"
        for pack in content.packages:
            defFunc += pack + "_"
        defFunc += content.classs + "_" + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to definition
        params = extractStuff.getMethodParams(content.methods[i])
        print(params)

        defFunc += " (JNIEnv* env, jclass object"
        for j in range(len(params)):
            if params[j] == "char" : defFunc += ", jbyte v" + str(j)
            elif params[j] == "short" : defFunc += ",  jshort v" + str(j)
            elif params[j] == "int": defFunc += ", jint v" + str(j)
            elif params[j] == "long": defFunc += ", jlong v" + str(j)
            elif params[j] == "float": defFunc += ", jfloat v" + str(j)
            elif params[j] == "double": defFunc += ", jdouble v" + str(j)
            elif params[j] == "wchar_t": defFunc += ", jchar v" + str(j)
            elif params[j] == "bool": defFunc += ", jboolean v" + str(j)
            elif params[j] == "std::wstring": defFunc += ", jstring v" + str(j)
        defFunc += ")\n"

        # Getting cpp function
        cppFunc = ""
        for pack in content.packages:
            cppFunc += pack + "."
        cppFunc += content.classs + "." + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to cpp function TODO

        lineString += (
        "\n" + 
        defFunc + 
        "{\n" +
        "    return " + cppFunc + "}\n"
        )

    print(lineString)