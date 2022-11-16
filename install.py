import sys
import os
import shutil

def main():
    name = "pylenium"
    folder = "\\pylenium\\"
    dest = sys.exec_prefix + "\\lib" + folder
    current = os.getcwd() + folder
    if os.path.exists(dest):
        print(f"you have already installed {name}.")
        return

    os.mkdir(dest)
    print("made directory")

    for file in os.listdir(current):
        if os.path.isfile(current + file):
            shutil.copy((current + file), dest)
            print("copied file")

    print("INSTALLED SUCCESSFULLY.")

if __name__ == "__main__":
    main()