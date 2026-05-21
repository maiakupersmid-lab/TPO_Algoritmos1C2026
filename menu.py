import funciones

def opciones_menu():
    print("Bienvenido al menú de algoritmos. Escriba el número de la opción que desea ejecutar:")
    print("1. Cargar nuevo contenido")
    print("2. Modificar contenido existente")
    print("3. Dar de baja contenido")
    print("4. Mostrar listado general de contenido")
    print("5. Salir")

def menu():
    opciones_menu()
    opcion = int(input("Opción: "))
    while opcion < 1 or opcion > 5:
        print("Error, debe ser entre 1 y 5")
        opciones_menu()
        opcion = int(input("Seleccione una opcion"))
    return opcion

def main():
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
            funciones.altaContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion ==2:
            print("Modificar")
            funciones.modificarContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion==3:
            print("Dar de baja")
            funciones.bajaContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 4:
            print("Listado general")
            funciones.listarContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        opcion = menu()

    print("Gracias por usar el programa")

main()