__author__ = 'febel'
class Vehiculo:
    def __init__(self, posicion=0):
        self._posicion = posicion
    def avance(self, distancia=1):
        self._posicion+= distancia
        print("Avance de", distancia)
    def getPosition(self):
        return self._posicion

class Car(Vehiculo):	# Inheritance (Herencia)
    def marchaAtras(self, distancia=1):
        self._posicion-= distancia
        print("Marcha atrás de", distancia)

assert issubclass(Car, Vehiculo)
print('Car es una sub-clase de Vehiculo.')

c1 = Car(1)
print('c1 is of type:', type(c1))
print('c1:', c1)
print('Posición de c1 : %d' % c1.getPosition())
c1.avance(2)
print('Posición de c1 :', c1.getPosition())
c1.marchaAtras(1)
print('Posición de c1 :', c1.getPosition())

v1 = Vehiculo(0)
print('v1 is of type:', type(v1))
print('v1:', v1)
try:
	v1.marchaAtras(1)
except AttributeError as e:
	print('Un vehículo genérico no puede dar marcha atrás.')

c = Car
print('c is of type:', type(c))
print('c:', c)
