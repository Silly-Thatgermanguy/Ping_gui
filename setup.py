import subprocess
import sys


def check_pip():
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_ttkbootstrap():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "ttkbootstrap"], check=True)
        print("ttkbootstrap installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing ttkbootstrap: {e}")


if check_pip():
    print("pip is installed :3")
    install_ttkbootstrap()
else:
    print("pip is not installed. Please install Python and ensure pip is added to PATH.")
