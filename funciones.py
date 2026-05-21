def buscarCodigo(codigos, buscar):
    # Buscar la posicion del codigo en la lista, si no lo encuentra devuelve -1
    pos = -1
    i = 0
    while i < len(codigos) and pos == -1:
        if codigos[i] == buscar:
            pos = i
        i += 1
    return pos

def altaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):  
    cod=int(input("Ingrese codigo a registrar o -1 para finalizar: "))
    
    # Verificar si quiere salir
    while cod != -1:
        
        # Verificar que el codigo no exista y sea positivo
        while cod <= 0 or buscarCodigo(codigos, cod) != -1:
            cod = int(input("El codigo ya existe o es invalido, reingrese: "))
        
        nom = input("Ingrese nombre de la pelicula o cancion a registrar: ").capitalize()       
        while nom == "":
            nom = input("No se puede ingresar un nombre vacio, reingrese: ").capitalize()
        
        tipo = input("Ingrese tipo (pelicula/cancion): ").lower()
        while tipo != "pelicula" and tipo != "cancion":
            tipo = input("Tipo ingresado no valido, reingrese: ").lower()
        
        if tipo == "pelicula":
            print("Generos: Terror - Comedia - Accion - Fantasia - Drama - Ciencia Ficcion - Romance") 
            genero = input("Ingrese genero: ") .capitalize()
            while genero != "Drama" and genero != "Comedia" and genero != "Accion" and genero != "Fantasia" and genero != "Terror" and genero != "Ciencia Ficcion" and genero != "Romance":
                genero = input("No se hallo el genero ingresado, reingrese: ").capitalize()

            clasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ") 
            while clasificacion != "ATP" and clasificacion != "+13" and clasificacion != "+16" and clasificacion != "+18":
                clasificacion = input("Clasificacion invalida, reingrese: ")
        else:
            print("Generos: Rap - Pop - Rock - Cumbia - Reggaeton - Hip Hop")
            genero = input("Ingrese genero: ").capitalize()
            while genero != "Rap" and genero != "Pop" and genero != "Rock" and genero != "Cumbia" and genero != "Reggaeton" and genero != "Hip Hop":
                genero = input("No se hallo el genero ingresado, reingrese: ").capitalize()
            
            clasificacion = "ATP"
        
        anio = int(input("Ingrese año: "))
        while anio <= 1900 or anio > 2026:
            anio = int(input("Año invalido, reingrese año: "))            
        
        codigos.append(cod)
        titulos.append(nom).capitalize()
        tipos.append(tipo).capitalize()
        generos.append(genero).capitalize()
        anios.append(anio)
        clasificaciones.append(clasificacion)
        print("Contenido agregado correctamente")
        cod=int(input("Ingrese nuevo codigo a registrar o -1 para finalizar: "))

def modificarContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a modificar: "))
    pos = buscarCodigo(codigos, buscar)

    if pos == -1:
        print("No existe contenido con ese codigo")
    else:
        print("Contenido encontrado:" , titulos[pos])
        nuevoTitulo = input("Nuevo titulo: ")
        while nuevoTitulo == "":
            nuevoTitulo = input("No se puede ingresar un nombre vacio, reingrese: ")
        titulos[pos] = nuevoTitulo.capitalize()
        
        nuevoTipo = input("Ingrese tipo (pelicula/cancion): ").lower()
        while nuevoTipo != "pelicula" and nuevoTipo != "cancion":
            nuevoTipo = input("Tipo ingresado no valido, reingrese: ").lower()
        tipos[pos] = nuevoTipo

        if nuevoTipo == "pelicula":
            print("Generos: Terror - Comedia - Accion - Fantasia - Drama - Ciencia Ficcion - Romance")
            nuevoGenero = input("Ingrese genero: ")
            while nuevoGenero != "Drama" and nuevoGenero != "Comedia" and nuevoGenero != "Accion" and nuevoGenero != "Fantasia" and nuevoGenero != "Terror" and nuevoGenero != "Ciencia Ficcion" and nuevoGenero != "Romance":
                nuevoGenero = input("No se hallo el genero ingresado, reingrese: ")
            
            nuevaClasificacion = input("Ingrese clasificacion (ATP/+13/+16/+18): ")
            while nuevaClasificacion != "ATP" and nuevaClasificacion != "+13" and nuevaClasificacion != "+16" and nuevaClasificacion != "+18":
                nuevaClasificacion = input("Clasificacion invalida, reingrese: ")
        else:
            print("Generos: Rap - Pop - Rock - Cumbia - Reggaeton - Hip Hop")
            nuevoGenero = input("Ingrese genero: ")
            while nuevoGenero != "Rap" and nuevoGenero != "Pop" and nuevoGenero != "Rock" and nuevoGenero != "Cumbia" and nuevoGenero != "Reggaeton" and nuevoGenero != "Hip Hop":
                nuevoGenero = input("No se hallo el genero ingresado, reingrese: ")
            
            nuevaClasificacion = "ATP"
        generos[pos] = nuevoGenero.capitalize()
        clasificaciones[pos] = nuevaClasificacion

        nuevoAnio = int(input("Nuevo año: "))
        while nuevoAnio <= 1900 or nuevoAnio > 2026:
            nuevoAnio = int(input("Año invalido, reingrese año: "))
        anios[pos] = nuevoAnio

        print("Contenido modificado correctamente")

    
def bajaContenido(codigos, titulos, tipos, generos, anios, clasificaciones):
    buscar = int(input("Ingrese codigo a eliminar: "))
    pos = buscarCodigo(codigos, buscar)
    
    if pos == -1:
        print("No se encontro el contenido")
    else:
        print("Titulo:", titulos[pos])
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
    print("Listado general de contenido:")    
    for i in range(len(codigos)):
        print(codigos[i], titulos[i], tipos[i], generos[i], anios[i], clasificaciones[i])