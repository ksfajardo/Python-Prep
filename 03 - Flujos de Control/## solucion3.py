## solucion3

a=10
if (a>0):
    print('La variable es mayor a 0')
elif (a<0):
    print('La variable es menor a 0')
else:
    print('La variable es 0')

b=13
c='15'
if (type(b)==type(c)):
    print('Las variables contienen el mismo tipo de daato')
else:
    print('Las variables contienen diferentes tipos de datos')

for x in range(1,21):
    if (x%2==0):
        print ('Es numero par')
    else:
        print('Es numero impar')

for y in range(1,5):
    print(y**3)

x=10
for i in range(x):
    print(i)

n=4
factorial=1
while (n > 0):
    for j in range(1,n+1):
        factorial *=j
    print (factorial)
    n -= 1

e=1
suma=0
for d in range(5):
    while (e<d):
        suma +=1
        e +=1
    print(suma)

cont=2
while(cont<30):
    primo=True
    for f in range(2,cont):
        if (cont%f==0):
            primo=False
            break
    if (primo):
        print (cont)
    cont +=1
   
## pues si se podria si se mirara cuanto tiempo menos demora el pc en hacerlo

n=100 
while (n<=300):
    if (n%12!=0):
        n+=1
        continue
    else: 
        print(n)
        n+=1 

n=2
quiere=1
while (quiere==1):
    primo=True
    for h in range(2,n):
        if (n%h==0):
            primo=False
            break
    if (primo):
        print ('El numero '+str(n)+' es primo. Desea encontrar el siguiente? ponga 1 para si y 0 para no')
        quiere=int(input())
    n +=1   
        
n=100
while (n<=300):
    if (n%3==0 and n%6==0):
        print ('el primer numero es '+ str(n))
        break
    else:
        n +=1


