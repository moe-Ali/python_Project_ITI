from os import system
import sys

#function to install python packages 
def install_python_package(package):
    system(" ".join([sys.executable,"-m","pip","install",package]))
    
#main function to install all packages needed to run php into the os
def main_install(package_manager,version):
    system(" ".join(["sudo",package_manager,"update -y"]))
    system(" ".join(["sudo",package_manager,"install -y httpd]"]))
    system(" ".join(["sudo",package_manager,"install -y mysql-server"]))
    system(" ".join(["sudo",package_manager,f"install -y php{version}"]))
    system("echo Done")