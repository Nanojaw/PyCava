def generate (filename, hFilename, content):
    lineString = f"#include <string>\n#include <{filename}.h>\n#include <{hFilename}>\n"

    # Getting the functions in the header which javac created
    hFuncs = []

    JNIFile = open(hFilename, 'r')
    JNILines = JNIFile.readlines()
    for i in range(len(JNILines)):
        if JNILines[i].startswith("JNIEXPORT"):
            last = 0
            line = list(JNILines[i + 1])
            for j in range(JNILines[i + 1].count(',') + 1):
                comma = JNILines[i + 1].find(',', last)
                line.insert(comma, f" v{j}")
                last = comma + 1

            JNILines[i + 1] = "".join(line)

            hFuncs.append(JNILines[i] + " " + JNILines[i + 1])

    for i in range(len(hFuncs)):
        # Getting cpp function
        cppFunc = ""
        for pack in content.packages:
            cppFunc += pack + "."
        cppFunc += content.classs + "." + content.methods[i][content.methods[i].find(" ") + 1:]

        #TODO Make parameters work

        lineString += (
        "\n" + 
        hFuncs[i][:len(hFuncs[i])-2] + 
        "\n{\n" +
        "    return " + cppFunc + "}\n"
        )

    print(lineString)