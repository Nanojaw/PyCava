import converter

def getPackages(filename: str) -> list[str]:
        file = open(f"{filename}")

        packageLine = file.readline()

        packages = packageLine[8:len(packageLine) - 2].split('.')

        return packages

def getClass(filename: str) -> str:
    file = open(f"{filename}")

    lines = file.readlines()

    classs = (list(filter(lambda x: "class" in x, lines)))[0]

    return classs[13: len(classs) - 3]

def getMethods(filename: str) -> list[str]:
    file = open(f"{filename}")

    lines = file.readlines()

    methodLines = list(filter(lambda x: "public native" in x, lines))

    for i in range(len(methodLines)):
        methodLines[i] = methodLines[i][len("    public native "):]
        firstParenthesis = methodLines[i].find("(")
        secondParenthesis = methodLines[i].find(")")

        if (firstParenthesis + 1 != secondParenthesis):
            methodLines[i] = converter.JavaMethodToCpp(methodLines[i])

    return methodLines

def getMethodParams(method: str) -> list[str]:
    firstParenthesis = method.find('(')
    secondParenthesis = method.find(')')

    if (firstParenthesis + 1 == secondParenthesis): return []

    paramsString = method[firstParenthesis + 1 : secondParenthesis]

    paramsArray = paramsString.split(',')

    for i in range(len(paramsArray)):
        paramsArray[i] = paramsArray[i].strip()
        paramsArray[i] = paramsArray[i][: paramsArray[i].find(' ')]
        if(paramsArray[i] == 'long'): paramsArray[i] = 'long long'

    return paramsArray

class javaContents:
    packages: list[str]
    classs: str
    methods: list[str]
    def __init__(self, filename):
        self.packages = getPackages(filename)

        self.classs = getClass(filename)

        self.methods = getMethods(filename)