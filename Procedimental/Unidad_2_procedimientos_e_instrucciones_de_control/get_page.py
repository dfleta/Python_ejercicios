import urllib

def get_page(url):
	pagina = urllib.urlopen(url)
	codigoHtml = pagina.read()
	pagina.close()
	return codigoHtml


print get_page('http://xkcd.com/353')