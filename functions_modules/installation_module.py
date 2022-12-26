from os import system
import sys

#function to install python packages 
def install_python_package(package):
    system(" ".join([sys.executable,"-m","pip","install",package]))
    print(f"\n\nPython Script: {package} installed\n\n")
    
#main function to install all packages needed to run php into the os
def main_install(package_manager,version,apache,sql,php):
    system(" ".join(["sudo",package_manager,"update -y"]))
    print("\n\nPython Script: Packages Update is Done\n\n ")
    
    system(" ".join(["sudo",package_manager,f"install -y {apache}"]))
    print(f"\n\nPython Script: Apache({apache}) Installed\n\n ")
    
    system(" ".join(["sudo",package_manager,f"install -y {sql}"]))
    print(f"\n\nPython Script: SQL({sql}) Installed\n\n ")
    
    system(" ".join(["sudo",package_manager,f"install -y {php}{version}"]))
    print(f"\n\nPython Script: PHP({php}{version}) Installed \n\nPython Script: completed!")
