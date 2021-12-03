"""
JaLora
"""
import os
import json
# Definicion de funciones
def menu(): # Funcion del menu principal, tenemos un if recursivo que comprueba la opcion que se va a seleccionar.
    os.system("clear")
    #
    print("===Menu===\n1. Gestion de Vehiculos\n2. Gestion de Rutas\n3. Gestion de Viajes\n4. Salir\n===Menu=== ")
    opcion=str(input("Escribe una opcion: "))
    if opcion == "1":   
        opc1()
    elif opcion == "2":
        opc2()
    elif opcion == "3":
        opc3()
    elif opcion == "4":
        input("Saliendo...")
    else:
        input("Selecciona una opcion correcta...")
        menu()

def submenu1(): # Funcion del submenu de la opcion 1. En el que tenemos un if recursivo que comprueba que opcion se va a seleccionar
    print("=========Submenu==========\na. Añadir nuevos vehiculos\nb. Eliminar vehiculos\nc. Listar flota de vehiculos\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca1()
        #Limpiar y bucle
        os.system("clear")
        submenu1()
    elif segundo == "b":
        opcb1()
        #Limpiar y bucle
        os.system("clear")
        submenu1()
    elif segundo == "c":
        opcc1()
        #Limpiar y bucle
        os.system("clear")
        submenu1()
    elif segundo == "z":
        input("Volviendo al menu principal.....")
        menu()
    else:
        print("Selecciona una opcion correcta")
        submenu1()
def submenu2(): # Funcion del submenu de la opcion 2. En el que tenemos un if recursivo que comprueba que opcion se va a seleccionar
    print("=======Submenu=========\na. Alta de rutas\nb. Baja de rutas\nc. Listar rutas\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca2()
        #Limpiar y bucle
        os.system("clear")
        submenu2()
    elif segundo == "b":
        opcb2()
        #Limpiar y bucle
        os.system("clear")
        submenu2()
    elif segundo == "c":
        opcc2()
        #Limpiar y bucle
        os.system("clear")
        submenu2()
    elif segundo == "z":
        print("Volviendo al menu principal...")
        menu()
    else:
        print("Selecciona una opcion correcta")
        submenu2()
def submenu3(): # Funcion del submenu de la opcion 1. En el que tenemos un if recursivo que comprueba que opcion se va a seleccionar
    print("=======Submenu=========\na. Dar de alta un viaje.\nb. Mostrar viajes asignados a un vehículo\nc. Mostrar viajes por ruta.\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca3()
        #Limpiar y bucle
        os.system("clear")
        submenu3()
    elif segundo == "b":
        opcb3()
        #Limpiar y bucle
        os.system("clear")
        submenu3()
    elif segundo == "c":
        opcc3()
        #Limpiar y bucle
        os.system("clear")
        submenu3()
    elif segundo == "z":
        print("Volviendo al menu principal...")
        menu()
    else:
        print("Selecciona una opcion correcta")
        submenu3()

def opc1(): # Funcion para llamar al submenu 1
    #Limpiar y bucle
    os.system("clear")
    #
    print("===Gestion de Vehiculos===")
    submenu1()
    #
def opc2(): # Funcion para llamar al submenu 2
    #Limpiar y bucle
    os.system("clear")
    #
    print("===Gestion de Viajes===")
    submenu2()
    #
def opc3(): # Funcion para llamar al submenu 3
    #Limpiar y bucle
    os.system("clear")
    #
    print("===Gestion de Viajes===")
    submenu3()

def opca1(): # Funcion para la opcion "a" del submenu 1
    añadircoche={ # Lo primero que haremos es crear un diccionario vacio en el que existira una clave y un valor vacio
        "Matricula" : "",
        "Fecha de Matriculacion" : "",
        "Modelo" : "",
        "Marca" : "",
    }
    print("=== Añadir nuevos vehiculos===")
    # Añadiendo datos al diccionario, con varios input por teclado
    matricula=str(input("Escribe una matricula: "))
    fmat=str(input("Escribe una fecha: "))
    modelo=str(input("Escribe un modelo: "))
    marca=str(input("Escribe una marca: "))
    # Damos valores a las claves del diccionario.
    añadircoche["Matricula"] = matricula
    añadircoche["Fecha de Matriculacion"] = fmat
    añadircoche["Modelo"] = modelo
    añadircoche["Marca"] = marca
    # Comprobacion y listado
    print(f"Coche añadido: {añadircoche}")
    listacoche = str(añadircoche)
    lista2=[]
    lista2.append(listacoche)
    lista3 = str(lista2)
    # Escribir en archivo
    with open('coches.txt', 'a') as txt:
        txt.write(f"\n{lista3}")

    # Continuar
    input("Continuar:")
def opcb1(): # Funcion para la opcion "b" del submenu 1
    print("=== Eliminar Vehiculos===")
    boleano = str(input("Quieres que te enseñe los vehiculos (s/n): ")) # If para comprobar si queremos listar los vehiculos o no
    if boleano == "s":
        print("Enseñando...")
        opcc1()
    else :
        print("Pasando...")
    buscar=str(input("Pon la matricula del vehiculo que quieras eliminar: "))
    # Eliminamos la matricula que hemos escrito por teclado. Lo que realmente hace es buscar la linea que contenga lo que hemos añadido por teclado
    # Y escribe en su lugar una linea vacia
    with open("coches.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if buscar not in line:
                f.write(line)
        f.truncate() # La opcion truncate, limpia el documento.
def opcc1(): # Funcion para la opcion "c" del submenu 1
    print("=== Listar flota de vehiculos===")
    # Abrimos el documento coches.txt y enseñamos el contenido para listar los vehiculos
    with open('coches.txt', 'r') as txt:
        listado = txt.read()
        print(listado)
    #
    input("Continuo: ")

def opca2(): # Funcion para la opcion "a" del submenu 2
    # Basicamente el codigo es practicamente el mismo que la opcion "a" del submenu 1. Cambiando los nombres de las variables y toda la informacion necesaria
    print("=== Alta de rutas ===")
    #
    añadirruta={
        "Nombre" : "",
        "Origen" : "",
        "Destino" : "",
        "Distancia" : "",
    }
    # Añadiendo datos al diccionario
    nombre=str(input("Escribe un nombre: "))
    origen=str(input("Escribe un origen: "))
    destino=str(input("Escribe un destino: "))
    distancia=str(input("Escribe una distancia: "))
    añadirruta["Nombre"] = nombre
    añadirruta["Origen"] = origen
    añadirruta["Destino"] = destino
    añadirruta["Distancia"] = distancia
    añadirruta=str(añadirruta)
    # Comprobacion y listado
    print(f"Ruta añadido: {añadirruta}")
    listaruta = str(añadirruta)
    listaruta2=[]
    listaruta2.append(listaruta)
    listaruta3 = str(listaruta2)
    # Escribir en archivo
    with open('rutas.txt', 'a') as txt:
        txt.write(f"\n{listaruta3}")
    # Continuar
    input("Continuar:")
def opcb2(): # Funcion para la opcion "b" del submenu 2
    print("=== Bajas de rutas ===")
    # Esta opcion es igual que la opcion "b" del submenu 1. Cambiando los nombres de las variables y el documento
    boleano = str(input("Quieres que te enseñe las rutas (s/n): "))
    if boleano == "s":
        print("Enseñando...")
        opcc2()
    else :
        print("Pasando...")
    buscar=str(input("Pon el nombre de la ruta que quieras eliminar: "))
    with open("rutas.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if buscar not in line:
                f.write(line)
        f.truncate()
def opcc2(): # Funcion para la opcion "c" del submenu 2
    print("=== Listar rutas ===")
    # Esta opcion es igual que la opcion "c" del submenu 1. Cambiando los nombres de las variables y el documento
    with open('rutas.txt', 'r') as txt:
        listado = txt.read()
        print(listado)
    input("Continuar: ")

def opca3(): # Funcion para la opcion "a" del submenu 3
    print("=== Dar de alta un viaje ===")
    # Practicamente igual que la opcion "a" del submenu 1. Cambiando la informacion necesaria y el nombre de las variables
    añadirviaje={
        "Fecha" : "",
        "Hora" : "",
        "Ruta" : "",
        "Matricula coche" : "",
    }
    # Añadiendo datos al diccionario
    fecha=str(input("Escribe un fecha: "))
    hora=str(input("Escribe un hora: "))
    ruta=str(input("Escribe un ruta: "))
    matcoch=str(input("Escribe una matcoch: "))
    añadirviaje["Fecha"] = fecha
    añadirviaje["Hora"] = hora
    añadirviaje["Ruta"] = ruta
    añadirviaje["Matricula coche"] = matcoch
    # Comprobacion y listado
    print(f"viaje añadido: {añadirviaje}")
    listaviaje = str(añadirviaje)
    listaviaje2=[]
    listaviaje2.append(listaviaje)
    listaviaje3 = str(listaviaje2)
    # Escribir en archivo
    with open('viajes.txt', 'a') as txt:
        txt.write(f"\n{listaviaje3}")
    # Continuar
    input("Continuar:")
def opcb3(): # Funcion para la opcion "b" del submenu 3
    print("=== Mostrar viajes asignados a un vehiculo ===")
    # Aqui lo que hacemos es buscar dentro de la linea en el archivo viajes.txt, la cadena que escribamos por teclado
    matric=str(input("Escribe la matricula: "))
    with open("viajes.txt") as openfile:
        for line in openfile:
            if matric in line:
                print(line)
    #
    input("Continuo:")                   
def opcc3(): # Funcion para la opcion "c" del submenu 3
    print("=== Mostrar viajes por ruta ===")
    # Aqui lo que hacemos es buscar dentro de la linea en el archivo viajes.txt pero vamos a dividir cada linea por , para poder enseñar solamente los datos de 
    # la fecha y la matricula. Buscando por la ruta que hemos escrito por teclado
    rut=str(input("Escribe la ruta: "))
    with open("viajes.txt") as openfile:
        for line in openfile:
            if rut in line:
                div1=line.split(",")
                div1=div1[0:-3]
                div2=line.split(",")
                div2=div2[3]
                div1=str(div1)
                div1=div1.replace("}"," ").replace("]"," ").replace("["," ").replace("{"," ").replace("'"," ").replace("\\"," ").replace("\"", " ").replace(" ", "")
                # Los .replace son para formatear la salida de lo que queremos enseñar.
                div2=div2.replace("}"," ").replace("]"," ").replace("["," ").replace("{"," ").replace("'"," ").replace("\\"," ").replace("\"", " ").replace(" ", "")
                print(f"{div1},{div2}")
    #
    input("Continuar: ")

# Script Principal
menu()