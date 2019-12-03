from v2.client import Personnage

class Salvateur(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur, Jeu)
        self.accesChat = 1
        self.sauvePrecedent = ""
        self.role = 'salvateur'

    def protege(self, perso):
        if self.sauvePrecedent != perso and perso in self.Jeu.Village.keys():
            self.Emeteur.envoi(('protege %s' % perso).encode('Utf-8'))
            return True
        else:
            return False