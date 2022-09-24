#!/usr/bin/env python3

import os
import subprocess

def main():
    home = os.getenv('HOME')
    subprocess.call([
        f"{home}/Android/Sdk/ndk/21.4.7075529/ndk-build",
         "NDK_PROJECT_PATH=.", 
         "NDK_APPLICATION_MK=Application.mk",
         "APP_BUILD_SCRIPT=Android.mk",
         "NDK_LIBS_OUT=out",
         "NDK_OUT=out" ])

if __name__ == '__main__':
    main()
