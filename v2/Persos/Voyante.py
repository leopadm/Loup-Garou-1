from v2.client import Personnage

class Voyante(Personnage):

    def __init__(self, pseudo, Emeteur):
        Personnage.__init__(self, pseudo, Emeteur)
        self.accesChat = 1
        self.role = 'voyante'

    def regarde(self, perso):
        self.Emeteur.envoi(('regarde %s' % perso).encode('Utf-8'))

    def affiche(self, reste):
        print('')
        # affiche le nom et le role de la personne demandee par regarde
        # est appelee par recepteur.decompose()