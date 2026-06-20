def buscarEnLista(codigos, buscar):
    # Funcion que me permite buscar la posicion del codigo en la lista, si no lo encuentra devuelve -1
    #cambio de buscarElemento y buscarCodigo a buscarEnLista por lógica repetida, es una búsqueda en una lista.
    pos = -1
    i = 0
    while i < len(codigos) and pos == -1:
        if codigos[i] == buscar:
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
        while buscarEnLista(generosPeliculas, genero) == -1:
            genero = input("No se hallo el genero ingresado, reingrese: ").lower()

        clasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ").upper()
        while buscarEnLista(clasificacionesPeliculas, clasificacion) == -1:
            clasificacion = input("Clasificacion invalida, reingrese: ").upper()
    else:
        print("Generos de musica:", generosCanciones)
        genero = input("Ingrese genero: ").lower()
        while buscarEnLista(generosCanciones, genero) == -1:
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
    cod = int(input("Ingrese codigo a registrar o -1 para volver al menu: "))
    while cod != -1:
        # Verificar que el codigo no exista y sea positivo
        while cod <= 0 or buscarEnLista(codigos, cod) != -1:
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
    pos = buscarEnLista(codigos, buscar)
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
    pos = buscarEnLista(codigos, buscar)
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
    pos = buscarEnLista(codigos, buscar)
    if pos == -1:
        print("No se encontro contenido con ese codigo")
    else:
        print("Contenido encontrado:")
        mostrarContenido(codigos[pos], titulos[pos], tipos[pos], generos[pos], anios[pos], clasificaciones[pos])

def reportePorAnio(codigos, titulos, tipos, generos, anios, clasificaciones, descendente):
    """
    Funcion generalizada de reportePorAnio y el descendente, ahora con una bandera para identificar la opción elegida
    (ver el if del segundo for)
    
    Verificar si existe otra manera de realizarlo en vez de usar una bandera como parámetro
    """
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

            if not descendente and aniosOrd[i] > aniosOrd[j]:
                intercambiar(aniosOrd, i, j)
                intercambiar(codigosOrd, i, j)
                intercambiar(titulosOrd, i, j)
                intercambiar(tiposOrd, i, j)
                intercambiar(generosOrd, i, j)
                intercambiar(clasificacionesOrd, i, j)

            elif descendente and aniosOrd[i] < aniosOrd[j]:
                intercambiar(aniosOrd, i, j)
                intercambiar(codigosOrd, i, j)
                intercambiar(titulosOrd, i, j)
                intercambiar(tiposOrd, i, j)
                intercambiar(generosOrd, i, j)
                intercambiar(clasificacionesOrd, i, j)

    for i in range(len(codigosOrd)):
        mostrarContenido(codigosOrd[i], titulosOrd[i], tiposOrd[i], generosOrd[i], aniosOrd[i], clasificacionesOrd[i])


def reporteyFiltrado(codigos, titulos, tipos, generos, anios, clasificaciones, criterio, valor):
    """
    Esta funcion se crea gracias a generalizar reportePorTipo y reportePorGenero, pero se agrega 2 parámetros para identificar
    la opción elegida por el usuario (tipo o género) y el valor de esa opcion elegida (pelicula o cancion / rock o pop o etc...)
    """
    encontrados = 0
    for i in range(len(codigos)):
        if criterio == "tipo":
            if tipos[i] == valor:
                mostrarContenido(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])
                encontrados += 1

        elif criterio == "genero":
            if generos[i] == valor:
                mostrarContenido(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])
                encontrados += 1

    if encontrados == 0:
        print("No se encontraron contenidos")

def contadorPorTipo(tipos, mostrar):
    cantPeliculas = 0
    cantCanciones = 0

    for i in range(len(tipos)):
        if tipos[i] == "pelicula":
            cantPeliculas += 1
        elif tipos[i] == "cancion":
            cantCanciones += 1

    if mostrar:
        print("Cantidad de peliculas:", cantPeliculas)
        print("Cantidad de canciones:", cantCanciones)
    else:
        return cantPeliculas, cantCanciones

def reporteMatricialTipoClasificacion(tipos, clasificaciones, mostrar):
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0]]

    for i in range(len(tipos)):
        if tipos[i] == "pelicula":
            fila = 0
        else:
            fila = 1

        columna = buscarEnLista(clasificacionesPeliculas, clasificaciones[i])
        matriz[fila][columna] += 1

    if mostrar:
        print("REPORTE MATRICIAL TIPO x CLASIFICACIÓN")
        print("             ATP   +13   +16   +18")
        print("Película     ", end="")
        for j in range(4):
            print(f"{matriz[0][j]:5}", end="")
        print()
        print("Canción      ", end="")
        for j in range(4):
            print(f"{matriz[1][j]:5}", end="")
        print()
    else:
        return matriz

def buscarExtremosAnio(anios):
    posAntiguo = 0
    posReciente = 0

    for i in range(1, len(anios)):
        if anios[i] < anios[posAntiguo]:
            posAntiguo = i
        if anios[i] > anios[posReciente]:
            posReciente = i
    return posAntiguo, posReciente

def generoMasUsado(generos):
    listaGeneros = []
    
    for i in range(len(generos)):
        pos = -1
        for j in range(len(listaGeneros)):
            if listaGeneros[j][0] == generos[i]:
                pos = j
        if pos != -1:
            listaGeneros[pos][1] += 1
        else:
            listaGeneros.append([generos[i], 1])

    genero = listaGeneros[0][0]
    cantidad = listaGeneros[0][1]
    for i in range(len(listaGeneros)):
        if listaGeneros[i][1] > cantidad:
            genero = listaGeneros[i][0]
            cantidad = listaGeneros[i][1]

    return genero

def reporteEstadisticoGeneral(codigos, titulos, tipos, generos, anios, clasificaciones):
    if len(codigos) == 0:
        print("No existen contenidos cargados")
        return

    peliculas, canciones = contadorPorTipo(tipos, False)
    posAntiguo, posReciente = buscarExtremosAnio(anios)
    genero = generoMasUsado(generos)
    matriz = reporteMatricialTipoClasificacion(tipos, clasificaciones, False)

    print("REPORTE ESTADÍSTICO GENERAL")
    print("-" * 60)
    print("Cantidad total de contenidos:", len(codigos))
    print("Cantidad de películas:", peliculas)
    print("Cantidad de canciones:", canciones)
    print("-" * 60)
    print("Contenido más antiguo:")
    print("Título:", titulos[posAntiguo])
    print("Año:", anios[posAntiguo])
    print()
    print("Contenido más reciente:")
    print("Título:", titulos[posReciente])
    print("Año:", anios[posReciente])
    print("-" * 60)
    print("Género más utilizado:")
    print(genero)
    print("-" * 60)
    print("Cantidad por clasificación:")
    print(f"{'Clasificación':<15}{'Cantidad'}")
    print("-" * 30)
    print(f"{'ATP':<15}{matriz[0][0] + matriz[1][0]}")
    print(f"{'+13':<15}{matriz[0][1] + matriz[1][1]}")
    print(f"{'+16':<15}{matriz[0][2] + matriz[1][2]}")
    print(f"{'+18':<15}{matriz[0][3] + matriz[1][3]}")

def reporteFiltradoTipoAnio(codigos, titulos, tipos, generos, anios, clasificaciones):
    tipoBuscar = pedirTipo()
    anioDesde = pedirAnio()
    anioHasta = pedirAnio()
    while anioDesde > anioHasta:
        print("El año desde no puede ser mayor al año hasta")
        anioDesde = pedirAnio()
        anioHasta = pedirAnio()

    encontrados = 0

    print("REPORTE FILTRADO")
    print("Tipo seleccionado:", tipoBuscar)
    print("Año desde:", anioDesde)
    print("Año hasta:", anioHasta)
    print("-" * 80)
    print(f"{'Código':<8}{'Título':<20}{'Tipo':<12}{'Género':<18}{'Año':<8}{'Clasif.':<10}")
    print("-" * 80)

    for i in range(len(codigos)):
        if tipos[i] == tipoBuscar and anioDesde <= anios[i] <= anioHasta:
            print(f"{codigos[i]:<8}{titulos[i]:<20}{tipos[i]:<12}{generos[i]:<18}{anios[i]:<8}{clasificaciones[i]:<10}")
            encontrados += 1
    print("-" * 80)

    if encontrados == 0:
        print("No existen contenidos con esos filtros")
    else:
        print("Total encontrados:", encontrados)