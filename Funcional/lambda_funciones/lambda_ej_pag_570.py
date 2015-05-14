
# if elif else extebnso con lógica <=> lambda function



imitacionIfElif = {
	'cero': 	(lambda: argumento ** 0),
	'cuadrado': (lambda: argumento ** 2),
	'cubo':		(lambda: argumento ** 3)
}

argumento = 2

for mensaje in ['cero', 'cuadrado', 'cubo']:
	print( imitacionIfElif[mensaje]() )  
	# notar () al final del diccionario para que los valores se ejecuten como funciones

# ejemplo basico

f = lambda y, z: y + z
	# argumentos sin ()
	# una unica expresion en el bloque de codigo

print( f(1,1) ) #2
print( f(1,2) ) #3


# as anonymous (i.e., unnamed) functions. 
# In practice, they are often used as a way to inline a function definition, or to defer execution of a piece of code.