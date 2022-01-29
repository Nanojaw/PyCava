from operator import contains


CppToJNI = {
    'char': 'jbyte',
    'short': 'jshort',
    'int': 'jint',
    'long long': 'jlong',
    'float': 'jfloat',
    'double': 'jdouble',
    'wchar_t': 'jchar',
    'bool': 'jboolean',
    'std::wstring': 'jstring',
    'std::vector<char>': 'jcharArray',
    'std::vector<short>': 'jshortArray',
    'std::vector<int>': 'jintArray',
    'std::vector<long>': 'jlongArray',
    'std::vector<float>': 'jfloatArray',
    'std::vector<double>': 'jdoubleArray',
    'std::vector<bool>': 'jbooleanArray',
    'std::vector<std::wstring>': 'jobjectArray'
}

JavaToCpp = {
    # Primitives
    'void': 'void',
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

CppToJava = {
    'void': 'void',
    'char': 'byte',
    'short': 'short',
    'int': 'int',
    'long long': 'long',
    'float': 'float',
    'double': 'double',
    'wchar_t': 'char',
    'bool': 'boolean',
    'std::wstring': 'String',

    'std::vector<char>': 'byte[]',
    'std::vector<short>': 'short[]',
    'std::vector<int>': 'int[]',
    'std::vector<long long>': 'long[]',
    'std::vector<float>': 'float[]',
    'std::vector<double>': 'double[]',
    'std::vector<wchar_t>': 'char[]',
    'std::vector<bool>': 'boolean[]',
}

def JavaMethodToCpp(method: str) -> str:
    method = method.replace('(', ' (')
    split = method.split(' ')

    for i in range(len(split)):
        try: 
            java = split[i].strip(',;()')
            cpp = JavaToCpp[java]
            split[i] = split[i][:split[i].find(java)]+ cpp + split[i][split[i].find(java) + len(java):] + " "
        except KeyError:
            if(contains(split[i], ',')): split[i] += " "

    return "".join(split)