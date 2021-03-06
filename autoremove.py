#!/usr/bin/python3
import os, platform
def rpl(filename="autoremove.bat", remove=False, output=True): #stands for remove pip libs
    if platform.system() == "Windows":
        if os.path.isfile(filename):
            if not remove and output:
                os.system(filename + " n")
                print("\nsuccesfully uninstalled all pip libs")
            elif remove and output:
                os.system(filename + " y")
                print("\nsuccesfully uninstalled all pip libs without prompting for yes/no")
            elif remove and not output:
                os.system(filename + " y > nul")
                return ("\nsuccesfully uninstalled all pip libs without prompting for yes/no and without output")
            elif not remove and not output:
                print("\nERROR\nwithout output of the command you cannot response to the command\ninvalide option")
            else:
                print("\nERROR\n")
        else:
            print(f"{filename} is missing or it has an other name")
    elif platform.system() == "Linux":
        if filename == "autoremove.bat":
            filename = "autoremove.sh"
        if os.path.isfile(filename):
            os.system(f"chmod +x {filename}")
            if not remove and output:
                os.system(filename)
                print("\nsuccesfully uninstalled all pip libs")
            elif remove and output:
                os.system(filename + " y")
                print("\nsuccesfully uninstalled all pip libs without prompting for yes/no")
            elif remove and not output:
                os.system(filename + " y > /dev/nul")
                return ("\nsuccesfully uninstalled all pip libs without prompting for yes/no and without output")
            elif not remove and not output:
                print("\nERROR\nwithout output of the command you cannot response to the command\ninvalide option")
            else:
                print("\nERROR\n")
    elif platform.system() == "Darwin":
        if filename == "autoremove.bat":
            filename = "autoremove.apple"
        if os.path.isfile(filename):
            os.system(f"chmod +x {filename}")
            if not remove and output:
                os.system(filename)
                print("\nsuccesfully uninstalled all pip libs")
            elif remove and output:
                os.system(filename + " y")
                print("\nsuccesfully uninstalled all pip libs without prompting for yes/no")
            elif remove and not output:
                os.system(filename + " y > /dev/nul")
                return ("\nsuccesfully uninstalled all pip libs without prompting for yes/no and without output")
            elif not remove and not output:
                print("\nERROR\nwithout output of the command you cannot response to the command\ninvalide option")
            else:
                print("\nERROR\n")
    else:
        print("Unsupported OS")