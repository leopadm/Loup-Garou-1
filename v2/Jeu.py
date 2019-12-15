class Jeu(object):

    def __init__(self):
        self.Village = {}
        self.nbrGentils = 0
        self.nbrLoups = 0
        self.tours = []
        self.listeMortsPotentielles = []  # Liste des morts potentielle avant le vote du matin    |||| A effacer CHAQUE matin
        self.listeProteges = []           # Liste des proteges durant la nuit                     |||| A effacer CHAQUE matin

    def regarde(self, pseudo):
        try:
            role = self.Village[pseudo]
            return 'rregarde %s' % role
        except:
            return None

    def protege(self, pseudo):
        self.listeProteges.append(pseudo)

    def tue(self, pseudo):
        self.listeMortsPotentielles.append(pseudo)

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