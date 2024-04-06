import importlib.metadata
import subprocess
import os

def check_and_install_module():
    module_name = "colorama"
    try:
        importlib.metadata.version(module_name)
        print(f"{module_name} module is already installed.")
    except importlib.metadata.PackageNotFoundError:
        print(f"{module_name} module is not installed. Installing...")
        try:
            if os.name == "nt":
                subprocess.check_call(["pip3", "install", module_name])
            else:
                subprocess.check_call(["pip3", "install", module_name]) # uninstall with "pip3 uninstall colorama"
            print(f"{module_name} module is installed.")
        except subprocess.CalledProcessError as e:
            print(f"{module_name} module could not be installed. Error: {e}")

check_and_install_module()
