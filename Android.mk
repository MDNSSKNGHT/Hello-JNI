LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := hello-jni
LOCAL_SRC_FILES := \
	src/hello-jni.cpp

include $(BUILD_SHARED_LIBRARY)
