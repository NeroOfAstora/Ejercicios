"""
JaLora
"""
import os
def opc1():
    os.system("clear")
    #
    print("Rellenar:\n")
    lista=[]
    cadena=""
    while cadena != "xx":
        cadena=input("Introduce (xx salir): ")
        lista.append(cadena)
    lista.pop(-1)
    print(f"la lista es: {lista}")
    #
    input("Continuar: ")
def opc2():
    os.system("clear")
    #
    print("Insertar elemento")
    elemento=input("Elemento: ")
    lista=input("Lista: ")
    lista=[]
    lista.append(elemento)
    print(lista)
    #
    input("Continuar: ")
def opc3():
    os.system("clear")
    #
    print("Crear Tupla")
    lista=[]
    cadena=""
    while cadena != "0":
        cadena=input("Introduce (0 salir): ")
        lista.append(cadena)
    lista.pop(-1)
    print(f"La tupla: {tuple(lista)}")
        
    
    #
    input("Continuar: ")
def opc4():
    os.system("clear")
    #
    op=(1,2,3,4,5,6,7,8,10)
    tuple(op)
    print(f"La tupla: {op}")
    minimo= min(op)
    maximo= max(op)
    long= len(op)
    print(f"El minimo: {minimo}")
    print(f"El maximo: {maximo}")
    print(f"La longitud: {long}")
    #
    input("Continuar: ")

while True:
    os.system("clear")
    print("===Menu===\n1. Rellenar lista\n2. Insertar elemento\n3. Crear tupla\n4. Operaciones con tuplas\n5. Salir\n==Menu=== ")
    opcion=int(input("Escribe una opcion: "))
    if opcion == 1:   
        opc1()
    elif opcion == 2:
        opc2()
    elif opcion == 3:
        opc3()
    elif opcion == 4:
        opc4()
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("salir")