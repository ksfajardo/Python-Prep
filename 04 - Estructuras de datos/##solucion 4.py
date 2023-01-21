##solucion 4
ciudades=['Barranquilla','Berlin','New York','Buenos Aires','Sao Paulo','Madrid']
print(ciudades[1])
print(ciudades[1:4])
print(type(ciudades))
print(ciudades[2:])
print(ciudades[:4])
ciudades.append('Berlin','Londres')
ciudades.remove('Madrid')
ciudades.insert(3,'Roma')
ciudades.extend(['Tokyo', 'Hong Kong'])
print(ciudades.index('Berlin'))
x=ciudades.pop()
print(x)
print(ciudades*4)
numeros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(numeros[10:15])
print(20 in numeros)
print(30 in numeros)
elemento='Paris'
if (elemento in ciudades):
    print('El elemento ',elemento,' ya existia en la lista')
else:
    ciudades.append(elemento)
    print('El elemento ',elemento,' se agrego a la lista')
print(ciudades.count('Berlin'))
print(numeros.count(13))
numeroslista:list(numeros)
unidad, dos, tres=numeros
diccionario={   'Ciudad':ciudades,
                'Paises':['Alemania','Colombia','USA','Italia','Francia'],
                'Continente':['America','Europa','Asia','Oceania','Africa']}
print(diccionario.keys())
print(diccionario['Ciudad'])
