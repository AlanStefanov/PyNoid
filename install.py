import os
import subprocess
import sys

def install_requirements(venv_python):
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([venv_python, "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    print("Setting up the PyNoid project...")
    
    # Check if venv folder exists
    if not os.path.isdir("venv"):
        # Create virtual environment
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created.")

    # Determine the path to the Python executable in the virtual environment
    if os.name == 'nt':
        venv_python = os.path.join("venv", "Scripts", "python.exe")
    else:
        venv_python = os.path.join("venv", "bin", "python")

    # Install requirements using the virtual environment's Python
    install_requirements(venv_python)
    print("Requirements installed.")

    print("Setup complete. To run the game, use the following commands:")
    print("source venv/bin/activate" if os.name != 'nt' else "venv\\Scripts\\activate")
    print(f"{venv_python} src/main.py")

if __name__ == "__main__":
    main()
