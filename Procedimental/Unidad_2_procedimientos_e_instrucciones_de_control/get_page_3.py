
# Perhaps the most straightforward is the Python urllib.request module: 
# given an Internet address string—a URL, or Universal Resource Locator
# this module opens a connection to the specified server and returns a file-like object 
# ready to be read with normal file object method calls (e.g., read , readline ).

from urllib.request import urlopen

def get_page_3(url):
	pagina = urlopen(url)
	codigoHtml = pagina.read().decode('utf')
	pagina.close()
	return codigoHtml


print(get_page_3('http://xkcd.com/353'))