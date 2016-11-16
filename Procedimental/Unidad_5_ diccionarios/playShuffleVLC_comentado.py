
import random


## UTILIDADES DE DEPURACION ## 

# No utilizo casos test:
# Empleo invariantes (precondiciones y postcondiciones)
# para chequear el estado
# de las estructuras de datos que modifico.
# Utilizo funciones para chequear
# la validez de los datos devueltos por las rutinas
# con las responsabilidades principales.


def checkSeleccionaCancionRandom(cancion, libreria):

    # precondiciones
    assert isinstance(cancion, str)
    assert isinstance(libreria, dict)

    # compruebo si la cancion seleccionada esta en la libreria
    if cancion not in libreria:
        return False
    else:
        return True


def checkPlaySuffle(playList):

    assert isinstance(playList, dict)

    # creo una lista con los valores del diccionario playList,
    # es decir, los titulos de las canciones.
    listaCanciones = list(playList.values())

    # chequeo que cada titulo solo aparezca una vez en la lista
    for item in listaCanciones:
        if listaCanciones.count(item) > 1:
            return False
    return True


## RUTINAS DE UTILIDADES ## 


def seleccionaCancionRandom(libreria):

    assert isinstance(libreria, dict)

    # extraigo las claves del diccionario libreria
    # (que son los titulos de las canciones)
    # creo una lista con ellas y extraigo una
    # al azar
    tituloCancion = random.choice(list(libreria.keys()))

    # postcondicion
    assert checkSeleccionaCancionRandom(tituloCancion, libreria), "la cancion no es una clave del diccionario de canciones"

    return str(tituloCancion)


def iniciarPlayList(numeroCancion):

    # simulare que el diccionario playList es una lista playList[integer]
    # donde la clave es un numero entero que incremento cada vez
    # que añado una cancion a la playList
    claveDiccionarioPlayList = numeroCancion

    def appendCancion(cancion, playList):

        assert isinstance(playList, dict), "playList no es un diccionario"
        # la cancion no debe estar ya en la playList
        assert cancion not in list(playList.values())

        # closure: claveDiccionarioPlayList recuerda su ultimo valor
        # cada vez que invocamos a appendCancion()
        # De este modo, incremento la clave del diccionario en uno
        # y coloco la cancion en esa "posicion" de la lista que simula
        # el diccionario implementado de este modo.
        nonlocal claveDiccionarioPlayList
        claveDiccionarioPlayList += 1
        # asocio el valor titulo de la cancion a la clave integer
        playList[claveDiccionarioPlayList] = str(cancion)
        return claveDiccionarioPlayList

    return appendCancion


def imprimirCancionesReproducidas(playList):

    assert isinstance(playList, dict)

    # Recorro el objeto iterable view keys() del diccionario playList
    # Antes lo he ordenado.
    for numeroCancion in sorted(playList.keys()):
        # muestro la posicion en la que fue elegida la cancion
        # y el titulo de la cancion
        print(str(numeroCancion) + ": " + str(playList[numeroCancion]))


def lanzarVLC(libreria, playList):

    # Las canciones han de estar en un directorio llamado biblioteca
    # en el directorio de la aplicacion.
    # Han de ser expresamente las incluidas en el diccionario libreria.
    # La extensión a este  programa es incluir la capa de acceso a datos
    # para extraer los titulos de las canciones y las rutas
    # a los ficheros del fichero XML playlist.xspf que genera VLC
    # o Rhythmbox con las canciones de la biblioteca

    import subprocess
    import shlex
    import os

    linuxPathVLC = "/usr/bin/vlc"
    lineaComandoVLC = linuxPathVLC
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            rutaAccesoFichero = libreria[tituloCancion]["location"]
        except KeyError:
            print("la cancion " + str(tituloCancion) + " no se encuentra en la biblioteca")
        else:
            # compruebo si la ruta de acceso al fichero cancion es correcto
            if os.path.exists(str(rutaAccesoFichero)):
                # anhado la ruta de acceso a la cancion
                # a la linea de comandos para invocar a VLC
                lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    # Esta libreria optimiza la division de los strings que forman
    # la entrada de un comando en argumentos
    args = shlex.split(lineaComandoVLC)

    try:
        # lanzo el subproceso VLC con las opciones adecuada:
        # la ruta de acceso a las canciones de la playList
        procesoVLC = subprocess.Popen(args)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")


## FUNCION PRINCIPAL ## 


def playShuffle(libreria, playList):

    # precondicion
    assert isinstance(libreria, dict), "libreria no es un diccionario"

    numeroCancion = 0
    actualizarPlayList = iniciarPlayList(numeroCancion)

    comandoPulsado = 'p'  # input("boton: play (p) / stop (s): ")
    continuar = True

    while comandoPulsado == 'p' and continuar == True:

        cancion = seleccionaCancionRandom(libreria)

        if cancion not in list(playList.values()):
            numeroCancionActual = actualizarPlayList(cancion, playList)
            print("Seleccionada: " + str(playList[numeroCancionActual]))
            # comandoPulsado = input("boton: play (p) / stop (s): ")
        else:
            comandoPulsado == "p"

        if len(libreria) == len(playList):
            continuar = False
            print("Se han incluido todas las canciones en la biblioteca")

    # postcondicion
    assert checkPlaySuffle(playList), "cancion repetida"

    return True


## PROGRAMA PRINCIPAL ##


def playShuffleVLC(libreria, playList):

    playShuffle(libreria, playList)

    imprimirCancionesReproducidas(playList)

    lanzarVLC(libreria, playList)


playList = {}
# playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }


libreria = {"California_Uber_Alles.mp3":
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }

playShuffleVLC(libreria, playList)
