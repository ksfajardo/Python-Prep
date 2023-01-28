import sys 
import os
import datetime

if len(sys.argv)==4:
    temperatura=sys.argv[1]
    humedad=sys.argv[2]
    llovio=sys.argv[3]

    t=datetime.datetime.now()
    marca=datetime.datetime.timestamp(t)

    archivo=open('clase09_ej2.csv','a')
    archivo.write(str(marca)+','+str(temperatura)+','+str(llovio)+'\n')
    archivo.close()

else:
    print('Tiene que proporcionar un valor de temperatura en grados celsius, un valor de humedad y si llovio o no')


