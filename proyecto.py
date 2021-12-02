"""
JaLora
"""
import os
import json
# Definicion de funciones
def menu():
    #Limpiar
    os.system("cls")
    print("===Menu===\n1. Gestion de Vehiculos\n2. Gestion de rutas\n3. Gestion de Viajes\n4. Salir\n==Menu=== ")
    opcion=int(input("Escribe una opcion: "))
    if opcion == 1:   
        opc1()
    elif opcion == 2:
        opc2()
    elif opcion == 3:
        opc3()
    elif opcion == 4:
        input("Saliendo...")
    else:
        print("Selecciona una opcion correcta...")
        menu

def submenu1():
    print("======Submenu=======\na. Añadir nuevos vehiculos\nb. Eliminar vehiculos\nc. Listar flota de vehiculos\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca1()
        #Limpiar y bucle
        os.system("cls")
        submenu1()
    elif segundo == "b":
        opcb1()
        #Limpiar y bucle
        os.system("cls")
        submenu1()
    elif segundo == "c":
        opcc1()
        #Limpiar y bucle
        os.system("cls")
        submenu1()
    elif segundo == "z":
        input("Saliendo.....")
    else:
        print("Selecciona una opcion correcta")
        submenu1()
def submenu2():
    print("======Submenu=======\na. Alta de rutas\nb. Baja de rutas\nc. Listar rutas\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca2()
        #Limpiar y bucle
        os.system("cls")
        submenu2()
    elif segundo == "b":
        opcb2()
        #Limpiar y bucle
        os.system("cls")
        submenu2()
    elif segundo == "c":
        opcc2()
        #Limpiar y bucle
        os.system("cls")
        submenu2()
    elif segundo == "z":
        print("Saliendo...")
    else:
        print("Selecciona una opcion correcta")
        submenu2()
def submenu3():
    print("======Submenu=======\na. Dar de alta un viaje.\nb. Mostrar viajes asignados a un vehículo\nc. Mostrar viajes por ruta.\nz. Salir")
    segundo=str(input("Escribe una opcion: "))
    if segundo == "a":   
        opca3()
        #Limpiar y bucle
        os.system("cls")
        submenu3()
    elif segundo == "b":
        opcb3()
        #Limpiar y bucle
        os.system("cls")
        submenu3()
    elif segundo == "c":
        opcc3()
        #Limpiar y bucle
        os.system("cls")
        submenu3()
    elif segundo == "z":
        print("Saliendo...")
    else:
        print("Selecciona una opcion correcta")
        submenu3()

def opc1():
    #Limpiar y bucle
    os.system("cls")
    #
    print("===Gestion de Vehiculos===")
    submenu1()
    #
def opc2():
    #Limpiar y bucle
    os.system("cls")
    #
    print("===Gestion de Viajes===")
    submenu2()
    #
def opc3():
    #Limpiar y bucle
    os.system("cls")
    #
    print("===Gestion de Viajes===")
    submenu3()

def opca1():
    añadircoche={
        "Matricula" : "",
        "Fecha de Matriculacion" : "",
        "Modelo" : "",
        "Marca" : "",
    }
    print("=== Añadir nuevos vehiculos===")
    # Añadiendo datos al diccionario
    matricula=str(input("Escribe una matricula: "))
    fmat=str(input("Escribe una fecha: "))
    modelo=str(input("Escribe un modelo: "))
    marca=str(input("Escribe una marca: "))
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
def opcb1():
    print("=== Eliminar Vehiculos===")
    boleano = str(input("Quieres que te enseñe los vehiculos (s/n): "))
    if boleano == "s":
        print("Enseñando...")
        opcc1()
    else :
        print("Pasando...")
    buscar=str(input("Pon la matricula del vehiculo que quieras eliminar: "))
    with open("coches.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if buscar not in line:
                f.write(line)
        f.truncate()
def opcc1():
    print("=== Listar flota de vehiculos===")
    with open('coches.txt', 'r') as txt:
        listado = txt.read()
        print(listado)
    #
    input("Continuo: ")

def opca2():
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
def opcb2():
    print("=== Bajas de rutas ===")
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
def opcc2():
    print("=== Listar rutas ===")
    with open('rutas.txt', 'r') as txt:
        listado = txt.read()
        print(listado)
    input("Continuar: ")

def opca3():
    print("=== Dar de alta un viaje ===")
    #
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
def opcb3():
    print("=== Mostrar viajes asignados a un vehiculo ===")
    #
    matric=str(input("Escribe la matricula: "))
    with open("viajes.txt") as openfile:
        for line in openfile:
            if matric in line:
                print(line)
    #
    input("Continuo:")                   
def opcc3():
    print("=== Mostrar viajes por ruta ===")
    #
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
                div2=div2.replace("}"," ").replace("]"," ").replace("["," ").replace("{"," ").replace("'"," ").replace("\\"," ").replace("\"", " ").replace(" ", "")
                print(f"{div1},{div2}")
    #
    input("Continuar: ")

# Script Principal
menu()