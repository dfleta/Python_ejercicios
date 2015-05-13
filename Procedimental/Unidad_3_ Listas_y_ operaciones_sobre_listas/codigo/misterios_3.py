
from urllib.request import urlopen

def get_page_3(url):
	pagina = urlopen(url)
	codigoHtml = pagina.read().decode('utf')
	pagina.close()
	return codigoHtml