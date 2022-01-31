import extractStuff
import converter

def generateWrapper(filename: str, hFilename: str, content):
    lineString = f"#include <string>\n#include <{filename}.h>\n#include <{hFilename}>\n"

    #  Adding all of the functions to be wrapped
    for i in range(len(content.methods)):

        # Adding definition to functions in header file
        defFunc = converter.CppToJNI[content.methods[i][:content.methods[i].find(' ')]] + " Java_"
        for pack in content.packages:
            defFunc += pack + "_"
        defFunc += content.classs + "_" + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to definition
        params = extractStuff.getMethodParams(content.methods[i])

        defFunc += " (JNIEnv* env, jobject obj"
        for j in range(len(params)):
            defFunc += f", {converter.CppToJNI[params[j]]} v{str(j)}"
        defFunc += ")\n"


        # Getting cpp function
        cppFunc = ""
        for pack in content.packages:
            cppFunc += pack + "::"
        cppFunc += content.classs + "::" + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to cpp function
        reference = "" # Reference and release is for handling reference objects that require cleanup
        release = ""

        cppFunc += "("
        for j in range(len(params)):
            if params[j] == "std::wstring": 
                reference += f"    const wchar_t* r{str(j)} = (*env)->GetStringChars(env, v{str(j)}, nullptr);\n"
                cppFunc += f", std::wstring(r{str(j)})"
                release += f"    (*env)->ReleaseStringChars(env, v{str(j)}, r{str(j)});\n"
            if params[j].startswith('std::vector'):
                reference += f"    const {converter.CppToJava[params[j]].strip('[]')}* r{str(j)} = (*env)->Get{converter.CppToJava[params[j]].strip('[]').capitalize()}ArrayElements(env, v{str(j)}, 0);\n"
                cppFunc += f", std::vector(r{str(j)}, r{str(j)} + (*env)->GetArrayLength(env, v{str(j)}))"
                release += f"    (*env)->Release{converter.CppToJava[params[j]].strip('[]').capitalize()}ArrayElements(env, v{str(j)}, r{str(j)}, 0);\n"
            else:
                cppFunc += f", ({params[j]}) v{str(j)}"
        cppFunc += ");\n"
        if cppFunc.find(",") != -1: cppFunc = cppFunc[:cppFunc.find(",")] + cppFunc[cppFunc.find(",") + 2:]


        # Handling returning
        returntype = content.methods[i][:content.methods[i].find(' ')]

        if returntype == 'std::wstring':
            result = ("    auto string = (*env)->NewString(env, &result[0], result.size());\n"
                      "    return string;\n")
        elif returntype.startswith('std::vector'):
            result = (f"    {converter.CppToJNI[returntype]} array = (*env)->New{converter.CppToJava[returntype].strip('[]').capitalize()}Array(env, result.size());\n"
                      f"    (*env)->Set{converter.CppToJava[returntype].strip('[]').capitalize()}ArrayRegion(env, array, 0, result.size(), &result[0]);\n"
                      f"    return array;\n")
        else:
            result = f"    return ({converter.CppToJNI[returntype]})result;\n"


        lineString += (
        "\n" + 
        defFunc + 
        "{\n" +
        reference +
        "    auto result = " + cppFunc +
        release +
        result +
        "}\n"
        )

    file = open(f"Cava/{hFilename[:hFilename.find('.')]}.cpp", 'w')
    file.write(lineString)
    file.close()

def generateCppFile(filename: str, content):
    cppFile = open(f"{filename}.cpp", 'w')

    file = f"#include <Cava/{filename}.h>\n\n"

    for method in content.methods:
        namespace = " "
        for package in content.packages:
            namespace += package + "::"
        method = method[:method.find(' ')] + namespace + content.classs + "::" + method[method.find(' ') + 1:]
        method = method.replace(';', '')
        method += "{\n    \n}\n"
        file += method
    
    cppFile.write(file)
