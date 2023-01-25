# solucion7
class Vehiculo:
    def __init__(self,color,tipo,cilindraje):
        self.color= color
        self.tipo= tipo
        self.cilindraje= cilindraje
        self.velocidad=0
        self.direccion=0

    def acelerar(self,vel):
        self.velocidad += vel
    def frenar(self,vel):
        self.velocidad -= vel
    def doblar(self,grados):
        self.direccion +=grados
    def estado(self):
        print('el vehiculo va a ',self.velocidad,' y giro a ',self.direccion)
    def descripcion(self):
        print('el vehiculo es de color ', self.color,', de tipo ',self.tipo,' y tiene ',self.cilindraje,' litros de cilindraje')

ford=Vehiculo('rojo','automovil',1.6)
chev=Vehiculo('Plata','automovil',1.6)
bmw=Vehiculo('azul','camioneta',2)

ford.acelerar(50)
ford.frenar(40)
ford.doblar(30)
ford.estado()
ford.descripcion()

from modulo import *

x=Funcionesant([1,2,3,3,4])
print(x.repetido())

