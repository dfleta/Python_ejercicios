import urllib

def get_page(url):
	pagina = urllib.urlopen(url)
	codigoHtml = pagina.read()
	pagina.close()
	return codigoHtml