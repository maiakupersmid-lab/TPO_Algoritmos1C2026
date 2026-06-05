def buscarCodigo(codigos, buscar):
    # Funcion que me permite buscar la posicion del codigo en la lista, si no lo encuentra devuelve -1
    pos = -1
    i = 0
    while i < len(codigos) and pos == -1:
        if codigos[i] == buscar:
            pos = i
        i += 1
    return pos

def buscarElemento(lista, buscado):
    # Funcion que busca un elemento en una lista y devuelve su posicion
    pos = -1
    i = 0
    while i < len(lista) and pos == -1:
        if lista[i] == buscado:
            pos = i
        i += 1
    return pos

generosPeliculas = ["DRAMA", "COMEDIA", "ACCION", "FANTASIA", "TERROR", "CIENCIA FICCION", "ROMANCE"]
generosCanciones = ["RAP", "POP", "ROCK", "CUMBIA", "REGGAETON", "HIP HOP"]
clasificacionesPeliculas = ["ATP", "+13", "+16", "+18"]

def altaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    # Pido el codigo a registrar hasta que el usuario ingrese -1 para finalizar
    cod = int(input("Ingrese codigo a registrar o -1 para finalizar: "))
    while cod != -1:
        # Verificar que el codigo no exista y sea positivo
        while cod <= 0 or buscarCodigo(codigos, cod) != -1:
            cod = int(input("El codigo ya existe o es invalido, reingrese: "))

        # Empiezo a pedir los datos de carga y validarlos segun corresponda
        nom = input("Ingrese nombre de la pelicula o cancion a registrar: ")
        while nom == "":
            nom = input("No se puede ingresar un nombre vacio, reingrese: ")

        tipo = input("Ingrese tipo (pelicula/cancion): ").lower()
        while tipo != "pelicula" and tipo != "cancion":
            tipo = input("Tipo ingresado no valido, reingrese: ").lower()
        if tipo == "pelicula":
            print("Generos de pelicula:", generosPeliculas)
            genero = input("Ingrese genero: ").upper()
            while buscarElemento(generosPeliculas, genero) == -1:
                genero = input("No se hallo el genero ingresado, reingrese: ").upper()

            clasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ").upper()
            while buscarElemento(clasificacionesPeliculas, clasificacion) == -1:
                clasificacion = input("Clasificacion invalida, reingrese: ").upper()
        else:
            print("Generos de musica:", generosCanciones)
            genero = input("Ingrese genero: ").upper()
            while buscarElemento(generosCanciones, genero) == -1:
                genero = input("No se hallo el genero de musica ingresado, reingrese: ").upper()

            clasificacion = "ATP"

        anio = int(input("Ingrese año: "))
        while anio <= 1900:
            anio = int(input("Año invalido, reingrese año: "))

        # Agrego todos los datos que ingresaron a la lista que corresponda
        codigos.append(cod)
        titulos.append(nom)
        tipos.append(tipo)
        generos.append(genero)
        anios.append(anio)
        clasificaciones.append(clasificacion)

        print("Contenido agregado correctamente")
        # Vuelvo a pedir un nuevo codigo a registrar o -1 para finalizar
        cod = int(input("Ingrese nuevo codigo a registrar o -1 para finalizar: "))

def modificarContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    # Pido el codigo que desea modificar y busco la posicion en la que se encuentra
    buscar = int(input("Ingrese codigo a modificar: "))
    pos = buscarCodigo(codigos, buscar)
    if pos == -1:
        print("No existe contenido con ese codigo")
    else:
        print("Codigo:", codigos[pos])
        print("Titulo:", titulos[pos])
        print("Tipo:", tipos[pos])
        print("Genero:", generos[pos])
        print("Año:", anios[pos])
        print("Clasificacion:", clasificaciones[pos])

        nuevoTitulo = input("Nuevo titulo: ")
        while nuevoTitulo == "":
            nuevoTitulo = input("No se puede ingresar un nombre vacio, reingrese: ")
        titulos[pos] = nuevoTitulo

        nuevoTipo = input("Ingrese tipo (pelicula/cancion): ").lower()
        while nuevoTipo != "pelicula" and nuevoTipo != "cancion":
            nuevoTipo = input("Tipo ingresado no valido, reingrese: ").upper()
        tipos[pos] = nuevoTipo
        if nuevoTipo == "pelicula":
            print("Generos de pelicula:", generosPeliculas)
            nuevoGenero = input("Ingrese genero: ").upper()
            while buscarElemento(generosPeliculas, nuevoGenero) == -1:
                nuevoGenero = input("No se hallo el genero ingresado, reingrese: ").upper()

            nuevaClasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ").upper()
            while buscarElemento(clasificacionesPeliculas, nuevaClasificacion) == -1:
                nuevaClasificacion = input("Clasificacion invalida, reingrese: ").upper()
        else:
            print("Generos de musica:", generosCanciones)
            nuevoGenero = input("Ingrese genero: ").upper()
            while buscarElemento(generosCanciones, nuevoGenero) == -1:
                nuevoGenero = input("No se hallo el genero ingresado, reingrese: ").upper()

            nuevaClasificacion = "ATP"

        generos[pos] = nuevoGenero
        clasificaciones[pos] = nuevaClasificacion

        nuevoAnio = int(input("Nuevo año: "))
        while nuevoAnio <= 1900:
            nuevoAnio = int(input("Año invalido, reingrese año: "))
        anios[pos] = nuevoAnio

        print("Contenido modificado correctamente")

def bajaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a eliminar: "))
    pos = buscarCodigo(codigos, buscar)
    if pos == -1:
        print("No se encontro el contenido")
    else:
        print("Codigo:", codigos[pos])
        print("Titulo:", titulos[pos])
        print("Tipo:", tipos[pos])
        print("Genero:", generos[pos])
        print("Año:", anios[pos])
        print("Clasificacion:", clasificaciones[pos])

        check = input("Confirma que quiere eliminar este contenido? SI/NO: ").upper()
        while check != "SI" and check != "NO":
            check = input("Lo ingresado no es valido, reingrese SI o NO: ").upper()
        if check == "SI":
            codigos.pop(pos)
            titulos.pop(pos)
            tipos.pop(pos)
            generos.pop(pos)
            anios.pop(pos)
            clasificaciones.pop(pos)
            print("Contenido eliminado")
        else:
            print("Cancelado correctamente")

def listarContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    print("Codigo | Titulo | Tipo | Genero | Año | Clasificacion")
    for i in range(len(codigos)):
        print(codigos[i], "|", titulos[i], "|", tipos[i], "|", generos[i], "|", anios[i], "|", clasificaciones[i])

def buscarContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a buscar: "))
    pos = buscarCodigo(codigos, buscar)
    if pos == -1:
        print("No se encontro contenido con ese codigo")
    else:
        print("Contenido encontrado:")
        print("Codigo:", codigos[pos])
        print("Titulo:", titulos[pos])
        print("Tipo:", tipos[pos])
        print("Genero:", generos[pos])
        print("Año:", anios[pos])
        print("Clasificacion:", clasificaciones[pos])