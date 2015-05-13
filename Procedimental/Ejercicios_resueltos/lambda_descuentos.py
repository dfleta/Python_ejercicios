descuento = {
	'premium': 	lambda importe: importe * 20 / 100,
	'oferta': 	lambda importe: importe * 10 / 100,
	'regular':	lambda importe: importe * 0 / 100
}

precio = 10

for mensaje in ['premium', 'oferta', 'regular']:
	print( str( descuento[mensaje](precio) ) + '€' )  
	# notar () al final del diccionario para que los valores se ejecuten como funciones