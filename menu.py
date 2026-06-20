# Importo el archivo de funciones para poder llamarlas desde mi programa principal
import funciones

def opciones_menu():
    # Funcion que muestra las opciones del menu
    print("-" * 50)
    print("                 MENU DE CONTENIDOS")
    print("-" * 50)
    print("Seleccione una opcion:")
    print()
    print("1. Cargar nuevo contenido")
    print("2. Modificar contenido existente")
    print("3. Dar de baja contenido")
    print("4. Mostrar listado general de contenido")
    print("5. Buscar contenido por codigo")
    print("6. Mostrar reporte ordenado por año de lanzamiento")
    print("7. Mostrar reporte filtrado por tipo de contenido")
    print("8. Reporte por año descendente")
    print("9. Reporte por genero")
    print("10. Contador por tipo")
    print("11. Reporte matricial Tipo x Clasificacion")
    print("12. Reporte estadístico general")
    print("13. Reporte filtrado por tipo y año")
    print("14. Salir")
    print("-" * 50)

def menu():
    # Funcion que permite seleccionar una opcion del menu
    opciones_menu()
    opcion = int(input("Opción: "))
    # Validar que la opcion elegida este dentro de los rangos permitidos
    while opcion < 1 or opcion > 14:
        print("Error, la opcion elegida debe estar entre 1 y 14")
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
    clasificaciones = ["ATP", "+13", "ATP", "+18", "ATP", "ATP"]
    opcion = menu()    
    while opcion != 14:
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
            funciones.reportePorAnio(codigos, titulos, tipos, generos, anios, clasificaciones, False)
        elif opcion == 7:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por tipo seleccionado
            tipoBuscar = funciones.pedirTipo()
            funciones.reporteyFiltrado(codigos, titulos, tipos, generos, anios, clasificaciones, "tipo", tipoBuscar)
        elif opcion == 8:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por año descendente
            funciones.reportePorAnio(codigos, titulos, tipos, generos, anios, clasificaciones, True)
        elif opcion == 9:
            # Invoco a la funcion del archivo funciones.py para mostrar el contenido por género
            generoBuscar = input("Ingrese genero: ").lower()
            funciones.reporteyFiltrado(codigos, titulos, tipos, generos, anios, clasificaciones, "genero", generoBuscar)
        elif opcion == 10:
            # Invoco a la funcion del archivo funciones.py para contar el contenido por tipo
            funciones.contadorPorTipo(tipos, True)
        elif opcion == 11:
            # Invoco a la funcion del archivo funciones.py para mostrar el reporte matricial
            funciones.reporteMatricialTipoClasificacion(tipos, clasificaciones, True)
        elif opcion == 12:
            # Invoco a la funcion del archivo funciones.py para mostrar el reporte estadistico general
            funciones.reporteEstadisticoGeneral(codigos, titulos, tipos, generos, anios, clasificaciones)
        elif opcion == 13:
            # Invoco a la funcion del archivo funciones.py para mostrar el reporte filtrado por tipo y rango de años
            funciones.reporteFiltradoTipoAnio(codigos, titulos, tipos, generos, anios, clasificaciones)
        opcion = menu()
    # El usuario eligio salir, muestro mensaje de despedida
    print("Gracias por usar el programa")
# Llamo a la funcion main para ejecutar el programa
main()