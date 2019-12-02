from v2.client import Personnage

class Salvateur(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.accesChat = 1
        self.sauvePrecedent = ""

    def protege(self, perso):
        self.Emeteur.envoi(('protege %s' % perso).encode('Utf-8'))