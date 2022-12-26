import sys
import platform
from functions_modules.installation_module import install_python_package , main_install

#to check and get the number of arguments passed to the script
args=sys.argv
if len(args) >2:
    print("!Error! Number of arguments Must not be more than 1")
    exit()
elif len(args)==2:
    version=args[1]
else:
    version=""

#to get the operating system name and then run the main install function
try:
    if platform.system() == "Linux":
        install_python_package("distro")
        import distro
        if "Centos" in distro.name():
            main_install("yum",version)
        elif "Ubuntu" in distro.name():
            main_install("apt",version)
        else:
            print("!Error! This Script only Supports Centos and Ubuntu")
    else:
        print("!Error! This script Only Supports Linux OS")
except:
    sys.exc_info()[1]