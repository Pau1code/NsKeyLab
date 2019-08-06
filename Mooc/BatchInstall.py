import os
libs = {"numpy", "matplotlib", "sklearn", "pyinstaller", "requests"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed somehow")