from v2.client import Personnage

class Chasseur(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.accesChat = 1

    def tue(self, perso):
        self.Emeteur.envoi(('tue %s' % perso).encode('Utf-8'))