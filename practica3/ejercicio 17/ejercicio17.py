# 17- Realizar un módulo que permite seleccionar opciones para: crear carpeta, cambiar de carpeta
# abrir Paint y Calculadora de Windows.

import os
import subprocess


def create_directory(name):
    try:
        os.mkdir(name)
        print(f"La carpeta '{name}' se creó con éxito.")
    except FileExistsError:
        print(f"Error: La carpeta '{name}' ya existe.")
    except Exception as e:
        print(f"Error: {e}")


def change_directory(path):
    try:
        os.chdir(path)
        print(f"Cambiado al directorio: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: El directorio '{path}' no existe.")
    except Exception as e:
        print(f"Error: {e}")


def open_paint():
    try:
        paint_path = os.path.join(os.getenv('SystemRoot'), 'System32', 'mspaint.exe')

        subprocess.run([paint_path])
    except FileNotFoundError:
        print("La aplicacion Paint no se ha encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


def open_calculator():
    try:
        calc_path = os.path.join(os.getenv('SystemRoot'), 'System32', 'calc.exe')

        subprocess.run([calc_path])
    except FileNotFoundError:
        print("La aplicaion Calculadora no se ha encontrado.")
    except Exception as e:
        print(f"Error: {e}")
