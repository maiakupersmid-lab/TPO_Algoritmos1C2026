# Importo el archivo de funciones para poder llamarlas desde mi programa principal
import funciones

def opciones_menu():
    # Funcion que muestra las opciones del menu
    print("=" * 60)
    print("Bienvenido al menú de algoritmos. Escriba el número de la opción que desea ejecutar:")
    print("=" * 60)
    print("1. Cargar nuevo contenido")
    print("2. Modificar contenido existente")
    print("3. Dar de baja contenido")
    print("4. Mostrar listado general de contenido")
    print("5. Buscar contenido por codigo")
    print("6. Mostrar reporte ordenado por año de lanzamiento")
    print("7. Mostrar reporte filtrado por tipo de conenido")
    print("9. Reporte por año descendente")
    print("10. Reporte por genero")
    print("11. Contador por tipo")
    print("12. Salir")

def menu():
    # Funcion que permite seleccionar una opcion del menu
    opciones_menu()
    opcion = int(input("Opción: "))
    # Validar que la opcion elegida este dentro de los rangos permitidos
    while opcion < 1 or opcion > 12:
        print("Error, la opcion elegida debe estar entre 1 y 12")
        opciones_menu()
        opcion = int(input("Seleccione una opcion"))
    return opcion

def main():
    # Programa principal
    codigos = [1, 2, 3, 4, 5, 6]
    titulos = ["Titanic", "Shrek", "Despacito", "Avatar", "Bohemian Rhapsody", "Toy Story"]
    tipos = ["pelicula", "pelicula", "cancion", "pelicula", "cancion", "pelicula"]
    generos = ["drama", "comedia", "reggaeton", "fantasia", "rock", "ciencia ficcion"]
    anios = [1985, 2001, 2017, 2009, 1975, 1995]
    clasificaciones = ["ATP", "+13", "+16", "+18", "ATP", "ATP"]
    opcion = menu()    
    while opcion != 12:
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
        elif opcion == 5:
            print("Busqueda por codigo")
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por codigo
            funciones.buscarContenido(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 6:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido ordenado por año
            funciones.reportePorAnio(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 7:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por tipo seleccionado
            print("Reporte filtrado por tipo")
            funciones.reportePorTipo(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 9:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por año descendente
            funciones.reportePorAnioDesc(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 10:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por género
            funciones.reportePorGenero(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 11:
            # Invoco a la funcion del archivo funciones.py para contar el contenido por tipo
            funciones.contadorPorTipo(tipos)
        opcion = menu()
    # El usuario eligio salir, muestro mensaje de despedida
    print("Gracias por usar el programa")
# Llamo a la funcion main para ejecutar el programa
main()