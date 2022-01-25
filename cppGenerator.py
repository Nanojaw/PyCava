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
        defFunc += " (JNIEnv* env, jclass object"
        
        
        # Getting cpp function
        cppFunc = ""
        for pack in content.packages:
            cppFunc += pack + "."
        cppFunc += content.classs + "." + content.methods[i][content.methods[i].find(" ") + 1:content.methods[i].find("(")]

        # Adding parameters to cpp function

        #TODO Make parameters work

        lineString += (
        "\n" + 
        defFunc + 
        "\n{\n" +
        "    return " + cppFunc + "}\n"
        )

    print(lineString)