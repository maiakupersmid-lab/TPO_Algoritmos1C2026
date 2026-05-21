# Importo el archivo de funciones para poder llamarlas desde mi programa principal
import funciones

def opciones_menu():
    # Funcion que muestra las opciones del menu
    print("Bienvenido al menú de algoritmos. Escriba el número de la opción que desea ejecutar:")
    print("1. Cargar nuevo contenido")
    print("2. Modificar contenido existente")
    print("3. Dar de baja contenido")
    print("4. Mostrar listado general de contenido")
    print("5. Salir")

def menu():
    # Funcion que permite seleccionar una opcion del menu
    opciones_menu()
    opcion = int(input("Opción: "))
    # Validar que la opcion elegida este dentro de los rangos permitidos
    while opcion < 1 or opcion > 5:
        print("Error, la opcion elegida debe estar entre 1 y 5")
        opciones_menu()
        opcion = int(input("Seleccione una opcion"))
    return opcion

def main():
    # Programa principal
    codigos = []
    titulos = []
    tipos = []
    generos = []
    anios = []
    clasificaciones = []
    
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            print("Dar de alta")
            # Invoco a la funcion del archivo funciones.py para dar de alta un nuevo contenido
            funciones.altaContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion ==2:
            print("Modificar")
            # Invoco a la funcion del archivo funciones.py para modificar un contenido 
            funciones.modificarContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion==3:
            print("Dar de baja")
            # Invoco a la funcion del archivo funciones.py para dar de baja un contenido 
            funciones.bajaContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 4:
            print("Listado general")
            # Invoco a la funcion del archivo funciones.py para listar todos los contenidos
            funciones.listarContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        opcion = menu()
    # El usuario eligio salir, muestro mensaje de despedida
    print("Gracias por usar el programa")
# Llamo a la funcion main para ejecutar el programa
main()