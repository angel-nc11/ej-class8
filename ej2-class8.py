from pickle import *

class Vehiculo:

    def __init__(self, color, llantas):
        self.color = color
        self.llantas = llantas

    def __str__(self):
        return self.color + " " + self.llantas


toyota = Vehiculo("Negro", "4")
print(toyota)

archivo = open('vehiculo_toyota', 'w+b')

dump(toyota, archivo)

archivo.seek(0)
toyota2 = load(archivo)

print(toyota2)
archivo.close()