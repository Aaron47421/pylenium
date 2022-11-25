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

    pycache = True

    for file in os.listdir(dest):
        if os.path.isfile(dest + file):
            os.remove(dest + file)
            print("deleted file.")

        try:
            for file1 in os.listdir(dest + "__pycache__\\"):
                if os.path.isfile(dest + "__pycache__\\" + file1):
                    os.remove(dest + "__pycache__\\" + file1)
                    print("clearing pycache")

        except:
            print("pycache not found.")
            pycache = False

    if pycache:
        try:
            os.rmdir(dest + "__pycache__")
            print("removed pycache.")
        except:
            pass

    os.rmdir(dest)
    print("removed pylenium.")


    print("UNINSTALLED SUCCESSFULLY.")

if __name__ == "__main__":
    main()