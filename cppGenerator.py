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

        # Adding parameters to cpp function

        reference = "" # Reference and release is for handling reference objects that require cleanup
        release = ""

        cppFunc += "("
        for j in range(len(params)):
            if params[j] == "char" : cppFunc += ", (char)v" + str(j)
            elif params[j] == "short" : cppFunc += ",  (short)v" + str(j)
            elif params[j] == "int": cppFunc += ", (int)v" + str(j)
            elif params[j] == "long": cppFunc += ", (long long)v" + str(j)
            elif params[j] == "float": cppFunc += ", (float)v" + str(j)
            elif params[j] == "double": cppFunc += ", (double)v" + str(j)
            elif params[j] == "wchar_t": cppFunc += ", (wchar_t)v" + str(j)
            elif params[j] == "bool": cppFunc += ", (bool)v" + str(j)
            elif params[j] == "std::wstring": 
                reference += "    const wchar_t* r" + str(j) + " = (*env)->GetStringChars(env, v" + str(j) + ", nullptr);\n"
                cppFunc += ", std::wstring(r" + str(j) + ")"
                release += "    (*env)->ReleaseStringChars(env, v" + str(j) + ", r" + str(j) + ");\n"
        cppFunc += ")\n"

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

    file = open(filename +  ".cpp", 'w')
    file.write(lineString)
    file.close()