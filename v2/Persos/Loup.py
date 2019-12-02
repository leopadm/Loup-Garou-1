from v2.client import Personnage

class Loup(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.accesChat = 2

    def tue(self, perso):
        self.Emeteur.envoi(('tue %s' % perso).encode('Utf-8'))