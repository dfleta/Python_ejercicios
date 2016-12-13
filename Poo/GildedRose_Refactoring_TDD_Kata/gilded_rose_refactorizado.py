# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # qué items hay en este if? => clases
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# class Interface para añadir comportamientos:
# una promesa

class Interfaz():

    def update_quality(self):
        pass


class NormalItem(Item, Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        if self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
        assert self.quality >= 0, "quality de %s fuera de rango" % self.__class__.__name__

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.sell_in = self.sell_in - 1


class ConjuredItem(NormalItem, Interfaz):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.sell_in = self.sell_in - 1


class AgedBrie(Item):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality = 50
        assert self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.sell_in = self.sell_in - 1


class Sulfuras(Item, Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        assert self.quality != 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass
        # falla: self.quality = self.quality + 1


class Backstage(Item, Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality = 50
        assert self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.sell_in = self.sell_in - 1
