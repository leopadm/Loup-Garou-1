from socket import *
from json import


class Personnage(object):

    def __init__(self, pseudo, serveur, connexion):
        self.estVivant = True
        self.estProtege = False
        self.estMaire = False
        self.accesChat = 1
        self.pseudo = pseudo
        self.connexion = serveur

    def tuer(self):
        valide = False
        if self.estProtege != True:
            valide = True
        return valide

    def meurt(self):
        self.communique([])

    def vote(self, pseudo):
        pouvoir = 1
        if self.estMaire == True:
            pouvoir = 2
        self.communique(["vote", pseudo, str(pouvoir)])

    def communique(self, instructions):
        commande = instructions[0]
        for i in range(1, len(instructions)):
            commande = commande + " " + instructions[i]
        self.connexion.send(commande.encode('Utf-8'))
