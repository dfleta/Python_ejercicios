from misterios_3 import get_page_3


def extraerEnlacesPagina(pagina):

	posicionEnlace = pagina.find('<a href=')

	if posicionEnlace == -1:
		return None, 0

	posicionComillasIniciales = pagina.find('"', posicionEnlace)
	posicionComillasFinales   = pagina.find('"', posicionComillasIniciales + 1)

	url = pagina[ posicionComillasIniciales + 1 : posicionComillasFinales ]

	return url, posicionComillasFinales



def imprimirEnlacesPagina(pagina):

	url = pagina

	while url:
		
		url, posicionComillasFinales = extraerEnlacesPagina(pagina)
		
		print(url)
		pagina = pagina[posicionComillasFinales:]


imprimirEnlacesPagina(get_page_3('http://xkcd.com/353/'))