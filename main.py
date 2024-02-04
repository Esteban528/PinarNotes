from src.app import * 
from src.graphic import * 

print(

    """ 
    ____  _                  _   _       _            
    |  _ \(_)_ __   __ _ _ __| \ | | ___ | |_ ___  ___ 
    | |_) | | '_ \ / _` | '__|  \| |/ _ \| __/ _ \/ __|
    |  __/| | | | | (_| | |  | |\  | (_) | ||  __/\__ \\
    |_|   |_|_| |_|\__,_|_|  |_| \_|\___/ \__\___||___/
    """
)

menu = [
    {"key": 1, "content": "Ver notas."},
    {"key": 2, "content": "Agregar notas."},
    {"key": 3, "content": "Eliminar notas."},
    {"key": 0, "content": "Salir de la aplicación."},
]


def showMenu():
    for element in enumerate(menu):
        element = element[1]
        show(f"{element["key"]}. {element["content"]}")


def main ():
    showMenu()
    action = int(input("Selecciona una opción: "))
    action = proccessAction(action)
    if (action == "none"):
        show("Eres muy pendejo seleccionaste algo que no es válido")
    
main()

