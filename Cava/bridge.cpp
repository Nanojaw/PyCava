#include <string>
#include <bridge.h>
#include <pycava_bridge.h>

void Java_pycava_bridge_Log (JNIEnv* env, jclass object, jbyte v0,  jshort v1, jint v2, jlong v3, jfloat v4, jdouble v5, jchar v6, jboolean v7, jstring v8)
{
    const wchar_t* r8 = (*env)->GetStringChars(env, v8, nullptr);
    auto result = pycava.bridge.Log((char)v0, (short)v1, (int)v2, (long long)v3, (float)v4, (double)v5, (wchar_t)v6, (bool)v7, std::wstring(r8))
    (*env)->ReleaseStringChars(env, v8, r8);
    return result;
}

void Java_pycava_bridge_Hello (JNIEnv* env, jclass object)
{
    auto result = pycava.bridge.Hello()ycava.bridge.Hello()
    return result;
}
