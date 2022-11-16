import sys
import os
import shutil

def main():
    name = "pylenium"
    folder = "\\pylenium\\"
    dest = sys.exec_prefix + "\\lib" + folder
    current = os.getcwd() + folder
    if not os.path.exists(dest):
        print(f"{name} is not installed.")
        return


    for file in os.listdir(dest):
        if os.path.isfile(dest + file):
            os.remove(dest + file)
            print("deleted file.")

    os.rmdir(dest)
    print("deleted directory.")

    print("UNINSTALLED SUCCESSFULLY.")

if __name__ == "__main__":
    main()