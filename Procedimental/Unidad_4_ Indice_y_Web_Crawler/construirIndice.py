# encoding: utf-8


def actualizarKeywordIndice(index, keyword, url):

	# Busca una keyword en el indice
	# Si exite, añade la URL a la keyword: si existe la url, no debe añadirla
	# Si no existe, crea una entrada nueva en el indice

	for entrada in index:

		if keyword == entrada[0]:
			if url not in entrada[1]:
				entrada[1].append(url)
			return

	index.append([keyword, [url]])


def buscarKeyword(index, keyword):

	# Busca la keyword en el indice y devuelve las url asociadas 

	for entrada in index:
		if keyword == entrada[0]:
			return entrada[1]

	return []


def actualizarIndice(index, url, contenido):

	# Actualiza todas las keywords que aparecen en contenido (en una pagina)
	# y actualiza cada una de esas entradas en el indice:
	# mediante actualizaKeywordIndice() <=> actualiza sus url o anhade la keyword

	keywords = contenido.split()
	
	for keyword in keywords:
		actualizarKeywordIndice(index, keyword, url)


# Construir rutina visualizacion datos


# Casos test actualizarKeywordIndice
'''
index =[
		["yo", ["yo.com", "yo.es"]],
		["tu", ["tu.com", "tu.es"]],
		["el", ["el.com"]]]

actualizarKeywordIndice(index, "ella", "ella.es")
print(index)
print(buscarKeyword(index, "el"))
actualizarKeywordIndice(index, "el", "el.es")
print(index)


# Casos test buscarKeyword

print(buscarKeyword(index, "el"))
print(buscarKeyword(index, "otro"))


# Casos test actualizarIndice

# Una página es una lista (seria mejor una tupla) de la url y su contenido
pagina = ["el.es", "yo tu el ella"]

actualizarIndice(index, pagina[0], pagina[1])
print(index)
print(buscarKeyword(index, "el"))
'''