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

def pedirTitulo(mensaje):
    # Funcion reutilizable para pedir y validar el titulo del contenido
    titulo = input(mensaje)
    while titulo == "":
        titulo = input("No se puede ingresar un nombre vacio, reingrese: ")
    return titulo

def pedirTipo():
    # Funcion reutilizable para pedir y validar el tipo de contenido
    tipo = input("Ingrese tipo (pelicula/cancion): ").lower()
    while tipo != "pelicula" and tipo != "cancion":
        tipo = input("Tipo ingresado no valido, reingrese: ").lower()
    return tipo

def pedirGeneroYClasificacion(tipo):
    # Funcion reutilizable para pedir y validar el genero y clasificacion segun el tipo de contenido
    if tipo == "pelicula":
        print("Generos de pelicula:", generosPeliculas)
        genero = input("Ingrese genero: ").lower()
        while buscarElemento(generosPeliculas, genero) == -1:
            genero = input("No se hallo el genero ingresado, reingrese: ").lower()

        clasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ").upper()
        while buscarElemento(clasificacionesPeliculas, clasificacion) == -1:
            clasificacion = input("Clasificacion invalida, reingrese: ").upper()
    else:
        print("Generos de musica:", generosCanciones)
        genero = input("Ingrese genero: ").lower()
        while buscarElemento(generosCanciones, genero) == -1:
            genero = input("No se hallo el genero ingresado, reingrese: ").lower()
        clasificacion = "ATP"

    return genero, clasificacion

def pedirAnio():
    # Funcion reutilizable para pedir y validar el año de lanzamiento
    anio = int(input("Ingrese año: "))
    while anio <= 1900 or anio > 2026:
        anio = int(input("Año invalido, reingrese año: "))
    return anio

def intercambiar(lista, i, j):
    # Funcion reutilizable para intercambiar las listas
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def mostrarContenido(codigo, titulo, tipo, genero, anio, clasificacion):
    # Funcion reutilizable para mostrar el contenido en pantalla
    print("------------------------------")
    print("Codigo:", codigo)
    print("Titulo:", titulo)
    print("Tipo:", tipo)
    print("Genero:", genero)
    print("Año:", anio)
    print("Clasificacion:", clasificacion)

generosPeliculas = ["drama", "comedia", "accion", "fantasia", "terror", "ciencia ficcion", "romance"]
generosCanciones = ["rap", "pop", "rock", "cumbia", "reggaeton", "hip hop"]
clasificacionesPeliculas = ["ATP", "+13", "+16", "+18"]

def altaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    # Pido el codigo a registrar hasta que el usuario ingrese -1 para finalizar
    cod = int(input("Ingrese codigo a registrar o -1 para finalizar: "))
    while cod != -1:
        # Verificar que el codigo no exista y sea positivo
        while cod <= 0 or buscarCodigo(codigos, cod) != -1:
            cod = int(input("El codigo ya existe o es invalido, reingrese: "))

        # Empiezo a pedir los datos de carga y validarlos segun corresponda
        nom = pedirTitulo("Ingrese nombre de la pelicula o cancion a registrar: ")
        tipo = pedirTipo()
        genero, clasificacion = pedirGeneroYClasificacion(tipo)
        anio = pedirAnio()

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
        mostrarContenido(codigos[pos], titulos[pos], tipos[pos], generos[pos], anios[pos], clasificaciones[pos])

        titulos[pos] = pedirTitulo("Nuevo titulo: ")

        nuevoTipo = pedirTipo()
        tipos[pos] = nuevoTipo

        nuevoGenero, nuevaClasificacion = pedirGeneroYClasificacion(nuevoTipo)
        generos[pos] = nuevoGenero
        clasificaciones[pos] = nuevaClasificacion

        anios[pos] = pedirAnio()

        print("Contenido modificado correctamente")

def bajaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a eliminar: "))
    pos = buscarCodigo(codigos, buscar)
    if pos == -1:
        print("No se encontro el contenido")
    else:
        mostrarContenido(codigos[pos], titulos[pos], tipos[pos], generos[pos], anios[pos], clasificaciones[pos])

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
    for i in range(len(codigos)):
        mostrarContenido(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])

def buscarContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a buscar: "))
    pos = buscarCodigo(codigos, buscar)
    if pos == -1:
        print("No se encontro contenido con ese codigo")
    else:
        print("Contenido encontrado:")
        mostrarContenido(codigos[pos], titulos[pos], tipos[pos], generos[pos], anios[pos], clasificaciones[pos])

def reportePorAnio(codigos, titulos, tipos, generos, anios, clasificaciones):
    codigosOrd = []
    titulosOrd = []
    tiposOrd = []
    generosOrd = []
    aniosOrd = []
    clasificacionesOrd = []

    for i in range(len(codigos)):
        codigosOrd.append(codigos[i])
        titulosOrd.append(titulos[i])
        tiposOrd.append(tipos[i])
        generosOrd.append(generos[i])
        aniosOrd.append(anios[i])
        clasificacionesOrd.append(clasificaciones[i])

    for i in range(len(aniosOrd) - 1):
        for j in range(i + 1, len(aniosOrd)):
            if aniosOrd[i] > aniosOrd[j]:
                intercambiar(aniosOrd, i, j)
                intercambiar(codigosOrd, i, j)
                intercambiar(titulosOrd, i, j)
                intercambiar(tiposOrd, i, j)
                intercambiar(generosOrd, i, j)
                intercambiar(clasificacionesOrd, i, j)

    print("REPORTE ORDENADO POR AÑO DE LANZAMIENTO")
    for i in range(len(codigosOrd)):
        mostrarContenido(codigosOrd[i], titulosOrd[i], tiposOrd[i], generosOrd[i], aniosOrd[i], clasificacionesOrd[i])

def reportePorTipo(codigos, titulos, tipos, generos, anios, clasificaciones):
    tipoBuscar = pedirTipo()
    encontrados = 0
    print("REPORTE FILTRADO POR TIPO")
    for i in range(len(codigos)):
        if tipos[i] == tipoBuscar:
            mostrarContenido(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron contenidos para el tipo seleccionado")

def reportePorAnioDesc(codigos, titulos, tipos, generos, anios, clasificaciones):
    codigosOrd = []
    titulosOrd = []
    tiposOrd = []
    generosOrd = []
    aniosOrd = []
    clasificacionesOrd = []

    for i in range(len(codigos)):
        codigosOrd.append(codigos[i])
        titulosOrd.append(titulos[i])
        tiposOrd.append(tipos[i])
        generosOrd.append(generos[i])
        aniosOrd.append(anios[i])
        clasificacionesOrd.append(clasificaciones[i])

    for i in range(len(aniosOrd) - 1):
        for j in range(len(aniosOrd) - 1 - i):
            if aniosOrd[j] < aniosOrd[j + 1]:
                intercambiar(aniosOrd, j, j + 1)
                intercambiar(codigosOrd, j, j + 1)
                intercambiar(titulosOrd, j, j + 1)
                intercambiar(tiposOrd, j, j + 1)
                intercambiar(generosOrd, j, j + 1)
                intercambiar(clasificacionesOrd, j, j + 1)

    print("REPORTE ORDENADO POR AÑO (DESCENDENTE)")
    for i in range(len(codigosOrd)):
        mostrarContenido(codigosOrd[i], titulosOrd[i], tiposOrd[i], generosOrd[i], aniosOrd[i], clasificacionesOrd[i])

def reportePorGenero(codigos, titulos, tipos, generos, anios, clasificaciones):
    generoBuscar = input("Ingrese genero a filtrar: ").lower()
    while buscarElemento(generosPeliculas, generoBuscar) == -1 and buscarElemento(generosCanciones, generoBuscar) == -1:
        generoBuscar = input("Genero invalido, reingrese: ").lower()
    encontrados = 0
    print("REPORTE FILTRADO POR GENERO")
    for i in range(len(codigos)):
        if generos[i] == generoBuscar:
            mostrarContenido(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron contenidos para ese genero")

def contadorPorTipo(tipos):
    cantPeliculas = 0
    cantCanciones = 0
    for i in range(len(tipos)):
        if tipos[i] == "pelicula":
            cantPeliculas += 1
        elif tipos[i] == "cancion":
            cantCanciones += 1
    print("Cantidad de peliculas:", cantPeliculas)
    print("Cantidad de canciones:", cantCanciones)