/*
 * Simple usage example of the Java Native Interface (JNI)
 */
#include <jni.h>

JNIEXPORT jstring JNICALL Java_com_example_hellojni_HelloJni_stringFromJNI(JNIEnv *env, jobject self) {
	return env->NewStringUTF("Hello from JNI!");
}
