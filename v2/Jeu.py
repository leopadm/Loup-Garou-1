class Jeu(object):

    def __init__(self):
        self.Village = {}
        self.nbrGentils = 0
        self.nbrLoups = 0
        self.tours = []

    def regarde(self, pseudo):
        role = self.Village[pseudo]
        return 'rregarde %s' % role

    def protege(self, pseudo):
        print('')

    def tue(self, pseudo):
        print('')

    def tourSuivant(self):
        print('')

    def removePerso(self, pseudo):
        try:
            del self.Village[pseudo]
            return True
        except:
            return False

    def ajoutPerso(self, reste):
        pseudo, role = reste.split()
        self.Village[pseudo] = role

    def updateMorts(self):
        print('')