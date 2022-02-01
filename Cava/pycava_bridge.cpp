#include <string>
#include "bridge.h"
#include "pycava_bridge.h"

JNIEXPORT jintArray JNICALL Java_pycava_bridge_Log (JNIEnv* env, jobject obj, jcharArray v0, jshort v1, jintArray v2, jlong v3, jfloat v4, jdouble v5, jchar v6, jboolean v7, jstring v8)
{
    const byte* r0 = (*env)->GetByteArrayElements(env, v0, 0);
    const int* r2 = (*env)->GetIntArrayElements(env, v2, 0);
    const wchar_t* r8 = (*env)->GetStringChars(env, v8, nullptr);
    auto result = pycava::bridge::Log(std::vector(r0, r0 + (*env)->GetArrayLength(env, v0)), (short) v1, std::vector(r2, r2 + (*env)->GetArrayLength(env, v2)), (long long) v3, (float) v4, (double) v5, (wchar_t) v6, (bool) v7, std::wstring(r8));
    (*env)->ReleaseByteArrayElements(env, v0, r0, 0);
    (*env)->ReleaseIntArrayElements(env, v2, r2, 0);
    (*env)->ReleaseStringChars(env, v8, r8);
    jintArray array = (*env)->NewIntArray(env, result.size());
    (*env)->SetIntArrayRegion(env, array, 0, result.size(), &result[0]);
    return array;
}

JNIEXPORT void JNICALL Java_pycava_bridge_Hello (JNIEnv* env, jobject obj)
{
    pycava::bridge::Hello();
}
