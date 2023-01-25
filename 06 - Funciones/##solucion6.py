##solucion6
def primo(numero):
    '''
    Devuelve si un numero es primo true y false si no lo es 
    '''
    p=True
    for i in range(2,numero):
        if (numero%i==0):
            p=False
            break
    return p
        
def lisprim(lista):
    '''
    Devuelve lista con primos de otra lista
    '''
    prim=[i for i in lista if primo(i)==True]
    return prim

def repetido(lista):
    '''
    Devuelve el numero que mas se repite
    '''
    cont=0
    for c in lista:
        if (lista.count(c)>=cont):
            cont=lista.count(c)
            elemento=c
    return elemento, cont

def minmax(lista, x=input('Ingrese 0 si quiere conocer el numero que menos se repite y 1 si quiere conocer el que mas se repite:')):
    '''devuelve el numero que mas se repite o el que menos se repite'''
    if (x==1):
        cont=0
        for c in lista:
            if (lista.count(c)>=cont):
                cont=lista.count(c)
                elemento=c
        return elemento, cont
    elif (x==0):
        cont=1
        for c in lista:
            if (lista.count(c)<=cont):
                cont=lista.count(c)
                elemento=c
        return elemento, cont

def temperatura(t,o,d):
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

def factorial(numero):
    if (type(numero)!= int or numero<0):
        print('El valor ingresado deber ser un entero positivo')
    else:
        fact=1
        for i in range(1,numero+1):
            fact *=i
        return fact









    


