from threading import Thread
from json import loads

class Personnage(Thread):

    def __init__(self, pseudo, Emeteur):
        Thread.__init__(self)
        self.estVivant = True
        self.estProtege = False
        self.estMaire = False
        self.accesChat = 1
        self.pseudo = pseudo
        self.Emeteur = Emeteur
        self.connexion = self.Emeteur.getConnexion()

        # format de Jeu : {"Village":{"pseudo1" : "role1", "pseudo2" : "role2", ...}, "nbrGentils" : 0", "nbrLoups": 0, "tours": []}
        self.Jeu = {}
        self.role = ''

    def tuer(self):
        valide = True
        if self.estProtege != True:
            valide = False
        return valide

    def meurt(self):
        print("")

    def vote(self, pseudo):
        pouvoir = 1
        if self.estMaire == True:
            pouvoir = 2

    def updateCopieJeu(self, nouveau):
        self.Jeu = loads(nouveau)