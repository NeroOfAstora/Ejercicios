'''
JaLora
'''
# === Imports ===
import os
# === Comandos ===
continua=0
diccionario={}
os.system("clear") # Comando para limpiar la terminal

while continua != "xxx":
    print("==============") # Esto es simplemente por estetica

    nombre=input("Escribe tu nombre: ") # Pedimos el nombre
    apellido= input("Escribe tus apellido: ") # Pedimos el apellido
    dni=input("Escribe tu DNI: ") # Pedimos el DNI
    contraseña=input("Escribe una contraseña: ")

    print("============")

    log=(nombre[0:2]) + (apellido[0:3]) + (dni[-3:]) # Aqui lo que hacemos es concatenar los valores que le indicamos siendo 
                                                 # el primer numero entre corchetes la posicion inicial y el ultimo 
                                                 # la posicion final.

    continua=input(f"Añade usuario: {log} enter para seguir: ")
    diccionario[log] = contraseña

    check=input(f"añadido usuario {log} salir o continua  (xxx-salir): ")
    if check != "xxx":
        pass
    else:
        break

print(diccionario)

# Final de Archivo