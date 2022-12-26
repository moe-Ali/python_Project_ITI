from os import system
import sys

#function to install python packages 
def install_python_package(package):
    system(" ".join([sys.executable,"-m","pip","install",package]))
    print(f"Python Script: {package} installed")
    
#main function to install all packages needed to run php into the os
def main_install(package_manager,version,apache,sql,php):
    system(" ".join(["sudo",package_manager,"update -y"]))
    print("Python Script: Packages Update is Done ")
    
    system(" ".join(["sudo",package_manager,f"install -y {apache}]"]))
    print(f"Python Script: Apache({apache}) Installed ")
    
    system(" ".join(["sudo",package_manager,f"install -y {sql}"]))
    print(f"Python Script: SQL({sql}) Installed ")
    
    system(" ".join(["sudo",package_manager,f"install -y {php}{version}"]))
    print(f"Python Script: PHP({php}{version}) Installed \n\n\n\n Python Script completed successfully!")
