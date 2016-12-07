
import xml.etree.ElementTree as ET

# origen datos fichero XML


def prepararObjetoDatos(data, xmlns):

    arbol = ET.parse(data)
    root = arbol.getroot()

    trackList = root.find("xmlns:trackList", xmlns)

    libreria = {track.find("xmlns:title", xmlns).text:
                    {
                     "artist": track.find("xmlns:creator", xmlns).text,
                     "album": track.find("xmlns:album", xmlns).text,
                     "location": track.find("xmlns:location", xmlns).text
                     } 
                     for track in trackList}

    return libreria


if __name__ == "__main__":
    '''
    Necesito este objeto en memoria:

    libreria = {"California_Uber_Alles.mp3":
                    {"track-number": 3,
                     "artist": "Dead Kennedys",
                     "album": "Dead Kennedys",
                     "location": "./biblioteca/California_Uber_Alles.mp3"},
                "Seattle_Party":
                    {"track-number": 1,
                     "artist": "Chastity Belt",
                     "album": "No regrets",
                     "location": "./biblioteca/Seattle_Party.flac"},
                "King_Kunta":
                    {"track-number": 3, "artist":
                     "Kendrick Lamar", "album":
                     "To Pimp A Butterfly",
                     "location": "./biblioteca/King_Kunta.mp3"}
                }
    '''

    # espacios de nombres de los elementos
    # del schema xspf (por defecto) y vlc
    #
    # Note that the standard parser discards namespace prefixes and
    # declarations, so if you need to access the prefixes later on (e.g. to
    # handle qualified names in attribute values or character data), you must
    # use an alternate parser.
    xmlns = {"xmlns": "http://xspf.org/ns/0/",
             "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/"}

    # origen de los datos: es un fichero XML
    # modo manual

    print('\n' + '#' * 5 + " MODO TEST MANUAL " + '#' * 5 + '\n')

    data = "listaPlayShuffleVLC.xspf"

    arbol = ET.parse(data)
    root = arbol.getroot()

    print("root: %s" % root.tag)

    print("trackList: %s " % root.find("xmlns:trackList", xmlns).tag)

    trackList = root.find("xmlns:trackList", xmlns)

    for track in trackList:
        print("title: %s" % track.find("xmlns:title", xmlns).text)
        print("creator: %s" % track.find("xmlns:creator", xmlns).text)
        print("album: %s" % track.find("xmlns:album", xmlns).text)
        print("lcoation: %s" % track.find("xmlns:location", xmlns).text)

    libreria = {track.find("xmlns:title", xmlns).text:
                {"artist": track.find("xmlns:creator", xmlns).text,
                 "album": track.find("xmlns:album", xmlns).text,
                 "location": track.find("xmlns:location", xmlns).text
                 }
                for track in trackList}

    print('\n' + '#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)

    # mediante prepararObjetoDatos()

    print('\n' + '#' * 5 + " TEST FUNCION ACCESO A DATOS " + '#' * 5 + '\n')

    data = "listaPlayShuffleVLC.xspf"

    libreria = {}

    xmlns = {"xmlns": "http://xspf.org/ns/0/",
             "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/"}

    libreria = prepararObjetoDatos(data, xmlns)

    print('#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)
