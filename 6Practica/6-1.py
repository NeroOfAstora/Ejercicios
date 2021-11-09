'''
JaLora
==========
Imports
==========
'''
import os
'''
========
Comandos
========
'''
os.system("clear")

frases=0
diccionario={}

while frases != "xxx":
    frases=input("Escribre la frase (xxx-salir): ")
    for i in frases.split(" "):
        if not diccionario.get(i):
            diccionario[i] = 0
    for i in frases.split(" "):
        diccionario[i] += 1

diccionario.pop("xxx")
print("=========")
print(diccionario)
print("=========")



# Final de Archivo