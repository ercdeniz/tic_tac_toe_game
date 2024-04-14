import threading
import subprocess
import os

def check_application():
    try:
        subprocess.run(["python3", "src/check_module.py"])
    except Exception as e:
        print(f"Error: {e}")

def remove_pycache():
    try:
        folder = os.path.join(os.getcwd(), "src", "__pycache__")
        if os.name == "nt":
            subprocess.run(["rd", "/s", "/q", folder], shell=True)
        else:
            subprocess.run(["rm", "-rf", folder])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        check_thread = threading.Thread(target=check_application)
        check_thread.start()
        check_thread.join()
        subprocess.run(["python3", "src/game.py"])
        remove_pycache()
    except KeyboardInterrupt:
        remove_pycache()
    except Exception as e:
        print(f"Error: {e}")
