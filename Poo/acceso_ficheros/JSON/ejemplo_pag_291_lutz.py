
# https://docs.python.org/3/library/json.html

import json


name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print('Diccionario rec: ', rec)

objetoSintaxisJSON_1 = json.dumps(rec)
print('objeto sintaxis JSON: ', objetoSintaxisJSON_1)

objetoSintaxisJSON_2 = json.loads(objetoSintaxisJSON_1)
print('objeto sintaxis JSON2')
print(objetoSintaxisJSON_2)

print(rec == objetoSintaxisJSON_2)

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)

print('lectura del fichero:')
print(open('testjson.txt').read())

P = json.load(open('testjson.txt'))
print('P: ')
print(P)

print('#### fichero JSON')
json.dump(rec, fp=open('testjson.json', 'w'), indent=4)
print('lectura del fichero:')
print(open('testjson.json').read())
P = json.load(open('testjson.json'))
print('P: ')
print(P)

print(type(P))

myfile = open('testjson.json', 'r')
print(type(myfile))

data = open('data_prototipo.json', 'r')
diccionario = json.load( data )

print(diccionario)