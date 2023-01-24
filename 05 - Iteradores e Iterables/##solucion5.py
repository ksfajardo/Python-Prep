##solucion5

lista= []
i=0
c=-15
while i<15:
    lista.append(c) 
    c +=1
    i +=1
print(lista)

i=0
while i<15:
    if (lista[i]%2==0):
        print(lista[i])
    i +=1

for elemento in lista:
    if (elemento%2==0):
        print(elemento)

for elemento1 in lista[:3]:
    print(elemento1)

for elem, c in enumerate(lista):
    print(elem,c)
    

nueva=[1,2,5,7,8,10,13,14,15,17,20]
i=1
while i<21:
    if (i not in nueva):
        nueva.insert(i-1,i)
    i+=1
print(nueva)

fibo=[0,1]
i=2
while i<30:
    c=fibo[i-2]+fibo[i-1]
    fibo.append(c)
    i +=1
print(fibo)

totalfibo=sum(fibo)
print(totalfibo)

i=29
while i>24:
    print(fibo[i-1]/fibo[i])
    i -=1

cadena='Hola Mundo. Esto es una practica del lenguaje de programación Python'
for enes,c in enumerate(cadena):
    if (c=='n'):
        print(enes)

diccionario={'clave1':'hola','clave2':'me da rabia','clave3':'que los ejercecios esten malos'}

for clave in diccionario:
    print(clave)

cad=list(cadena)
for letra in cad:
    print(letra)

a=['william','karla']
b=['salas','fajardo']
c= zip(a,b)
print(list(c))

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
divent7=[d for d in lis if d%7==0]
print(divent7)

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cuent=0
for e in lis:
    if (type(e)==list):
        cuent += len(e)
    else:
        cuent +=1
print (cuent)

for f,e in enumerate(lis):
    if (type(e)!=list):
        lis[f]= [e]
print(lis)     









