from misterios import get_page


def extraerEnlacesPagina(pagina):

	posicionEnlace = pagina.find('<a href=')

	if posicionEnlace == -1:
		return None, 0

	posicionComillasIniciales = pagina.find('"', posicionEnlace)
	posicionComillasFinales   = pagina.find('"', posicionComillasIniciales + 1)

	url = pagina[ posicionComillasIniciales + 1 : posicionComillasFinales ]

	return url, posicionComillasFinales



def imprimirEnlacesPagina(pagina):

	while True:
		
		url, posicionComillasFinales = extraerEnlacesPagina(pagina)
		
		if url:
			print url
			pagina = pagina[posicionComillasFinales:]

		else:
			break 


imprimirEnlacesPagina(get_page('http://xkcd.com/353/'))