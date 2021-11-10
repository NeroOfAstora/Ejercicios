'''
JaLora
'''
# === Imports ===
import os
# === Comandos ===
os.system("clear") # Comando para limpiar la terminal
print("==============") # Esto es simplemente por estetica
nombre=input("Escribe tu nombre: ") # Pedimos el nombre
apellido= input("Escribe tus apellido: ") # Pedimos el apellido
dni=input("Escribe tu DNI: ") # Pedimos el DNI
print("============")

log=(nombre[0:2]) + (apellido[0:3]) + (dni[-3:]) # Aqui lo que hacemos es concatenar los valores que le indicamos siendo 
                                                 # el primer numero entre corchetes la posicion inicial y el ultimo 
                                                 # la posicion final.
print(f"Tu login es el siguiente: {log}") # Mostramos por pantalla la variable que hemos almacenado con los valores anteriores
# Final de Archivo