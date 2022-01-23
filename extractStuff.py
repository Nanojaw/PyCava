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

    return methodLines

class javaContents:

    def __init__(self, filename):
        self.packages = getPackages(filename)

        self.classs = getClass(filename)

        self.methods = getMethods(filename)