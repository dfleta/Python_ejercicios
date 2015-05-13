# -*- encoding: utf-8 -*-

# autor: David Polo

import math

def areaEsfera (radioEsfera):
	return 4 * math.pi * radioEsfera ** 2


def volumenEsfera (radioEsfera):
	return 4 * math.pi * radioEsfera ** 3 / 3.0


radioEsfera = input ('Dame el radio de la esfera en metros de la que quieres saber su volumen y su área: ')

print 'el area de tu esfera es: ', areaEsfera (radioEsfera), ' m2'
print 'el volumen de tu esfera es: ', volumenEsfera (radioEsfera), 'm3'

# falta especificar los casos test