#solucion8
# 1. Posiblemnete de un error al momento de ejecutar el metodo que espera como input una lista y no lo deje ejecutar

import unittest
def temperatura(t,o,d):
    assert type(t)==float, f'{t} debe ser un numero'
    assert o == 'C' or 'F' or 'K', 'El origen debe ser C , K o F'
    assert d == 'C' or 'F' or 'K', 'El origen debe ser C , K o F'
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

class Funcionesant:
    def __init__(self, lista):
        if (type(lista)!=list):
            self.lista=[]
            raise ValueError('Se creo una lista vacia porque el elemento ingresado debe ser una lista de numeros enteros') 
        else:
            self.lista=lista
    
    def repetido(self):
        cont=0
        for c in self.lista:
            if ((self.lista).count(c)>=cont):
                cont=(self.lista).count(c)
                elemento=c
        return elemento, cont

    def primo(self):
        lista_primos=[]
        for i in self.lista:
            p=True
            for n in range(2,i):
                if (i%n==0):
                    p=False
                    break
            lista_primos.append(p)
                    
        return lista_primos

class PruebaDeCristalTest(unittest.TestCase):

    def test_creacion_objeto(self):
        lis = [1,2,2,2,3,4]

        res= Funcionesant(lis)
        
        self.assertEqual(res.lista, lis)

    def test_repetido(self):
        lis=[1,2,2,2,3,4]
        resultado=[2,3]
        res= Funcionesant(lis)
        moda,repet= res.repetido(lis)
        h=[moda,repet]
        self.assertEqual[resultado,h]

    def test_error(self):
        n=9
        self.assertRaises(ValueError,Funcionesant,n)



    

        