def getPackages(filename):
        file = open(f"../{filename}")

        packageLine = file.readline()

        packages = packageLine[8:len(packageLine) - 2].split('.')

        return packages

def getClass(filename):
    file = open(f"../{filename}")

    lines = file.readlines()

    classs = (list(filter(lambda x: "class" in x, lines)))[0]

    return classs[13: len(classs) - 3]

def getMethods(filename):
    file = open(f"../{filename}")

    lines = file.readlines()

    methodLines = list(filter(lambda x: "public static native" in x, lines))

    for i in range(len(methodLines)):
        methodLines[i] = methodLines[i][25:]
        firstParenthesis = methodLines[i].find("(")
        secondParenthesis = methodLines[i].find(")")

        if (firstParenthesis + 1 != secondParenthesis):
            methodLines[i] = methodLines[i].replace("String", "std::wstring")

            methodLines[i] = methodLines[i].replace("byte", "char")
            methodLines[i] = methodLines[i].replace("long", "long long")
            methodLines[i] = methodLines[i].replace("char", "wchar_t")
            methodLines[i] = methodLines[i].replace("bolean", "bool")

    return methodLines

def getMethodParams(method):
    firstParenthesis = method.find('(')
    secondParenthesis = method.find(')')

    if (firstParenthesis + 1 == secondParenthesis): return []

    paramsString = method[firstParenthesis + 1 : secondParenthesis]

    paramsArray = paramsString.split(',')

    for i in range(len(paramsArray)):
        paramsArray[i] = paramsArray[i][: paramsArray[i].find(' ')]

    return paramsArray

class javaContents:
    def __init__(self, filename):
        self.packages = getPackages(filename)

        self.classs = getClass(filename)

        self.methods = getMethods(filename)