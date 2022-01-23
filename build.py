#!/usr/bin/env python3

import os
import subprocess

# Compile in main function
def main():
    home = os.getenv('HOME')
    subprocess.call([
        f"{home}/android-ndk-r23b/ndk-build", 
         "NDK_PROJECT_PATH=.", 
         "NDK_APPLICATION_MK=./Application.mk",
         "APP_BUILD_SCRIPT := ./Android.mk"
    ])

if __name__ == '__main__': main()
