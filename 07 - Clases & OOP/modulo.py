#modulo
class Funcionesant:
    def __init__(self, lista):
        self.lista=lista
    
    def repetido(self):
        cont=0
        for c in self.lista:
            if ((self.lista).count(c)>=cont):
                cont=(self.lista).count(c)
                elemento=c
        return elemento, cont

    def primo(self,numero):
        p=True
        for i in range(2,numero):
            if (numero%i==0):
                p=False
                break
        return p
    
    def temperatura(self,t,o,d):
        if(o=='C'):
            if (d=='K'):
                temp= t+273.15
                return temp
            elif (d=='F'):
                temp=(t*9/5)+32
                return temp
        elif(o=='F'):
            if (d=='C'):
                temp==(t-32)*5/9
                return temp
            elif (d=='K'):
                temp=((t-32)*5/9)+273.15
        elif (o=='K'):
            if (d=='C'):
                temp=t-273.15
                return temp
            elif (d=='F'):
                temp= ((t-273.15)*9/5)+32
                return temp

    def factorial(self,numero):
        if (type(numero)!= int or numero<0):
            print('El valor ingresado deber ser un entero positivo')
        else:
            fact=1
            for i in range(1,numero+1):
                fact *=i
            return fact