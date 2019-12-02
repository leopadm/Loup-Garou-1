from v2.client import Personnage

class Sorciere(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.potionVie = True
        self.potionMort = True

    def tue(self, perso):
        self.Emeteur.envoi(('tue %s' % perso).encode('Utf-8'))

    def protege(self, perso):
        self.Emeteur.envoi(('protege %s' % perso).encode('Utf-8'))