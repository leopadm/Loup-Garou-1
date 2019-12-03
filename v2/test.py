class Edit(object):
    def __init__(self):
        self.value = 0

    def changeValue(self, new):
        self.value = new

    def readValue(self):
        return self.value


class Editeur(object):
    def __init__(self, Edit):
        self.Edit = Edit

    def editer(self, new):
        self.Edit.changeValue(new)

    def lire(self):
        return self.Edit.readValue()

LE = Edit()

edit1 = Editeur(LE)
edit2 = Editeur(LE)

print(LE.readValue())
edit1.editer(1)
print(edit2.lire())
edit1.editer(33)
print(edit2.lire())
