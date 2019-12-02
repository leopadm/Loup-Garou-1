from v2.client import Personnage

class Chaman(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.accesChat = 3