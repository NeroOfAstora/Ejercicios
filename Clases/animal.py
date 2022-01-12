class Animal:
    def __init__(self, especie,edad): 
        self.especie = especie
        self.edad = edad
    def hablar(self) :
        pass
    def moverse(self) -> None:
        pass
    def describeme(self) -> None:
        print("Soy un animal del tipo", type(self).__name__)
class Lito(Animal):
    pass    
perreto = Lito('Perro', 10)
perreto.describeme()