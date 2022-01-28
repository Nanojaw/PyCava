CppToJNI = {
    'char': "byte",
    'short': "jshort",
    'int': "jint",
    'long long': "jlong",
    'float': "jfloat",
    'double': "jdouble",
    'wchar_t': "jchar",
    'bool': "jboolean",
    'std::wstring': "jstring",
    'std::vector<char>': "jchararray",
    'std::vector<short>': "jshortarray",
    'std::vector<int>': "jintarray",
    'std::vector<long>': "jlongarray",
    'std::vector<float>': "jfloatarray",
    'std::vector<double>': "jdoublearray",
    'std::vector<bool>': "jbooleanarray",
    'std::vector<std::wstring>': "jobjectarray"
}

JavaToCpp = {
    # Primitives
    'byte': 'char',
    'short': 'short',
    'int': 'int',
    'long': 'long long',
    'float': 'float',
    'double': 'double',
    'char': 'wchar_t',
    'boolean': 'bool',
    'String': 'std::wstring',

    # Arrays
    'byte[]': 'std::vector<char>',
    'short[]': 'std::vector<short>',
    'int[]': 'std::vector<int>',
    'long[]': 'std::vector<long long>',
    'float[]': 'std::vector<float>',
    'double[]': 'std::vector<double>',
    'char[]': 'std::vector<wchar_t>',
    'boolean[]': 'std::vector<bool>'
}

def JavaMethodToCpp(method: str) -> str:
    method = method.replace('(', ' ')
    method = method.strip(',);')
    split = method.split(' ')
    i = 0
    while (i < len(split)):
        try: 
            split[i] = JavaToCpp[split[i]]
        except KeyError: 
            split.pop(i)
        i+=1

    return "".join(split)