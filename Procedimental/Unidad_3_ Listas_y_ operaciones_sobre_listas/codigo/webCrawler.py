# encoding: utf-8

from misterios_3 import get_page_3


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

	while toCrawl:
		
		url = toCrawl.pop()
		
		if url not in crawled:

			unirListas(toCrawl, listaEnlacesPagina(get_page_3(url)))
			crawled.append(url)

	return crawled


semilla = 'https://www.udacity.com/cs101x/index.html'

print(webCrawler(semilla))

# lista = listaEnlacesPagina(get_page_3(semilla))
# print(lista)