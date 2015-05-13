# encoding: utf-8

from get_page import get_page

from parseador import extraerKeywords

from construirIndice import actualizarIndice



def unirListas(listaP, listaQ):
	
	for elemento in listaQ:

		if elemento not in listaP:
			listaP.append(elemento)
		# else:
			# el elemento ya existe en la listaP y no lo añadimos
	return


def extraerEnlacesPagina(pagina):

	posicionEnlace = pagina.find('<a href=')

	if posicionEnlace == -1:
		return None, 0

	posicionComillasIniciales = pagina.find('"', posicionEnlace)
	posicionComillasFinales   = pagina.find('"', posicionComillasIniciales + 1)

	url = pagina[ posicionComillasIniciales + 1 : posicionComillasFinales ]

	return url, posicionComillasFinales



def listaEnlacesPagina(pagina):

	links = []

	while True:
		
		url, posicionComillasFinales = extraerEnlacesPagina(pagina)
		
		if url:
			links.append(url)
			pagina = pagina[posicionComillasFinales:]
		
		else:
			break

	return links



def webCrawler(seed):

	toCrawl = [seed]
	crawled = []

	index= []

	while toCrawl:
		
		url = toCrawl.pop()
		
		if url not in crawled:

			# dividir el contenido en keywords, y actualizar las keywords del indice con esa url

			# obtener el contenido de la pagina (keywords + HTML) como un string
			contenidoAsString = get_page(url)

			# extraer las keywords del contenido de la pagina => quitar HTML 
			keywords = extraerKeywords(url)

			actualizarIndice(index, url, keywords)

			unirListas(toCrawl, listaEnlacesPagina(contenidoAsString) )
			crawled.append(url)

	return index


semilla = 'https://www.udacity.com/cs101x/index.html'

print(webCrawler(semilla))



# datos = extraerKeywords(semilla)

# print(datos.split())

# lista = listaEnlacesPagina(get_page(semilla))
# print(lista)