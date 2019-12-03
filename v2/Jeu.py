class Jeu(object):

    def __init__(self):
        self.Village = {}
        self.nbrGentils = 0
        self.nbrLoups = 0
        self.tours = []

    def regarde(self, pseudo):
        role = self.Village[pseudo]
        return role

    def tourSuivant(self):
        print("")

    def removePerso(self, pseudo):
        del self.Village[pseudo]

    def updateMorts(self):
        print('')

    def ajoutPerso(self, reste):
        pseudo, role = reste.split()
        self.Village[pseudo] = role