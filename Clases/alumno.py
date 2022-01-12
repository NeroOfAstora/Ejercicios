class Alumno():
    def __init__(self,nombre,dni,nota):
        self.nombre = nombre
        self.dni = dni
        self.nota = nota 
    def descrip(self):
        if self.nota >= 5:
            print("Nombre: ",self.nombre,"Aprobado ", "Nota:", self.nota  )
        else :
            print("Nombre: ",self.nombre,"Suspenso ", "Nota:", self.nota)

def main():
    juan = Alumno('Juan',3245,5)
    juan.descrip()


main()