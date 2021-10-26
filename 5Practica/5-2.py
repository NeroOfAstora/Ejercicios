"""
JaLora
"""
import os
def opc1():
    suma=num1+num2
    print(f"El resultado es: {suma}")
    sigue=input("Continua: ")
def opc2():
    resta=num1-num2
    print(f"El resultado es: {resta}")
    sigue=input("Continua: ")

while True:
    os.system("clear")
    print("===Menu===\n1. Suma\n2. Resta\n3. Salte\n==Menu=== ")
    opcion=int(input("Escribe una opcion: "))
    if opcion != 3:
        num1=int(input("Num1: "))
        num2=int(input("Num2: "))
        if opcion == 1:
            opc1()
        elif opcion == 2:
            opc2()
        else:
            print("Error")
    elif opcion == 3:
        print("saliendo")
        break
    else:
        print("Error")