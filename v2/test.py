from json import *
from io import StringIO

class Edit(object):
    def __init__(self):
        self.value = 0
        self.byte = 3

    def changeValue(self, new):
        self.value = new

    def readValue(self):
        return self.value

    def __str__(self):
        return str(self.__dict__)

class Editeur(object):
    def __init__(self, Edit):
        self.Edit = Edit

    def editer(self, new):
        self.Edit.changeValue(new)

    def lire(self):
        return self.Edit.readValue()

    def __str__(self):
        return str(self.__dict__)

LE = Edit()

edit1 = Editeur(LE)
edit2 = Editeur(LE)

print(LE.__dict__)
print(type(dumps(LE.__dict__)))
print(dumps(LE.__dict__))
Jeu = loads('{}')
print(Jeu)