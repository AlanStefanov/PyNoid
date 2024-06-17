# PyNoid
Remake del famoso juego Akanoid
--------------
Prerequisitos:
Python 3+
pip
venv

Desarrollo:

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual

source venv/bin/activate

# Abrir juego
python src/main.py

# Crear el ejecutable con PyInstaller
pyinstaller --onefile --windowed src/main.py
