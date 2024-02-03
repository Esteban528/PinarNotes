# Para el sistema de notas de hoy, crearemos uno el cual, cada cosa que tenga sea una funcion, la cual estara dividida en 4, y empecemos por la mas importante
# Primero creamos el array en el cual se van a guardar cada nota que creemos

notas = []


# Luego crearemos la funcion menu, la cual nos va a dar las opciones, estas opciones dependiendo de cual se escoja tendra una funcion
print(

    """ 
    
.-----------------. .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || |     ____     | || |  _________   | || |      __      | || |    _______   | |
| ||_   \|_   _| | || |   .'    `.   | || | |  _   _  |  | || |     /  \     | || |   /  ___  |  | |
| |  |   \ | |   | || |  /  .--.  \  | || | |_/ | | \_|  | || |    / /\ \    | || |  |  (__ \_|  | |
| |  | |\ \| |   | || |  | |    | |  | || |     | |      | || |   / ____ \   | || |   '.___`-.   | |
| | _| |_\   |_  | || |  \  `--'  /  | || |    _| |_     | || | _/ /    \ \_ | || |  |`\____) |  | |
| ||_____|\____| | || |   `.____.'   | || |   |_____|    | || ||____|  |____|| || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    
    """
)
def Menu():
    while True:
        print("1. Agregar nota")
        print("2. Eliminar nota")
        print("3. Ver notas")
        print("4. Salir")
        opcion = str(input("Ingrese una opción: "))

        # Se le dice que hacer primero si se escoje una opcion y luego llamaremos las funciones que crearemos luego
        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            eliminar_nota()
        elif opcion == "3":
            ver_notas()
        elif opcion == "4":
            break
        else:
            print("No existe esta opcion")


# Esta es la funcion de agregar una nota (1) La cual esta compuesta de una variable la cual se encarga de guardar el input que ponga el usuario llamada titulo el cual
# sera el tutulo que contenga la nota y otra variable que guardara su contenido
def agregar_nota():
    titulo = input("Pon el titulo de la nota: ")
    contenido = input("Pon el contenido de la nota: ")
    # Estas dos variables componen una llamada "nota" la cual es igual al titulo y el contenido que tenga esta es decir esta guarda el titulo y el contenido y todo lo que hay
    # en ella se guarda en el array vacio de notas
    nota = {"titulo": titulo, "contenido": contenido}
    notas.append(nota)


# Ahora hacemos la funcion De eliminar notas, Esta se encargara de mirar si hay una nota, si no hay nada mostrara un mensaje el cual nos dira que el array esta vacio


def eliminar_nota():
    if not notas:
        print("No has escrito ninguna nota")
        return

    print("Lista de notas")
    # Ahora haremos dos variables que se encargaran de darnos el indice en el que esta cada nota y lo que hay en el indice, este saldra ennumerado, y se le sumara uno
    # Para que no comience desde el cero incluyendo que lo que hay en las notas salga el titulo
    for i, nota in enumerate(notas):
        print(f"{i + 1}. {nota['titulo']}")
        # Luego de esto le decimos que la variable indice sera un entero el cual nos ayudara a que solo sea de este tipo, luego el usuario pone el numero, si este numero que marca
        # Es el mismo que el del indice en el que esta la nota, la nota se borrara

    indice = int(input("Pon el número de la nota que desea eliminar: "))-1

    if not notas[indice]:
        print("El valor ingresado no es un número válido.")
    else:
        del notas[indice]


def ver_notas():
    if not notas:
        print("No hay notas para mostrar")
        return

    for i, nota in enumerate(notas):
        print(f"{i + 1}. {nota['titulo']}")
        
    indice = int(input("Pon el número de la nota que desees ver: ")) - 1
    print(notas[indice])

Menu()
