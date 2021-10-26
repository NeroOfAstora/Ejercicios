"""
JaLora
MENU
"""
import os
def opc1():
    print("1")
def opc2():
    print("Saliendo")

while True:
    os.system("clear")
    print("===Menu===\n1. Haz cosas\n2. Salte\n==Menu=== ")
    opcion=int(input("Escribe una opcion: "))
    if opcion == 1:
        opc1()
    elif opcion == 2:
        opc2()
        break
    else:
        print("Error")
    
   