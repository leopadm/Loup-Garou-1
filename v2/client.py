from threading import Thread
import socket, sys
from v2.Jeu import Jeu
from json import dumps, loads


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
        valide = False
        if self.estProtege != True:
            valide = True
        return valide

    def meurt(self):
        print("")

    def vote(self, pseudo):
        pouvoir = 1
        if self.estMaire == True:
            pouvoir = 2

    def updateCopieJeu(self, nouveau):
        self.Jeu = loads(nouveau)


class Emission(object):

    def __init__(self, HOST="192.168.1.20", PORT=8888):
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = HOST
        self.PORT = PORT

        try:
            self.connexion.connect((self.HOST, self.PORT))
        except socket.error:
            print('La liaison a echoue')
            sys.exit()
        print('Connecte au serveur')

    def envoi(self, colis):
        self.connexion.send(colis.encode('Utf-8'))

    def fermerConnection(self):
        self.connexion.close()

    def getConnexion(self):
        return self.connexion


class Reception(Thread):

    def __init__(self, Emetteur, Joueur):
        Thread.__init__(self)
        self.Emetteur = Emetteur
        self.Joueur = Joueur
        self.connexion = self.Emetteur.getConnexion()

    def run(self):
        while True:
            msgRecu = self.connexion.recv(1024).decode('Utf-8')
            print(msgRecu)
            if not msgRecu or msgRecu.upper() == 'FIN':
                self.connexion.send('FIN'.encode('Utf-8'))
                break
            self.Joueur.updateCopieJeu(msgRecu)
        self.Emetteur._stop()
        print('Connexion interrompue')
        self.connexion.close()

    def decompose(self, msg):
        commandList = ['rregarde', 'updateJeu']

        commande = -1
        reste = ''
        for i in range(len(commandList)):
            if msg[0:][:len(commandList[i])] == commandList[i]:
                commande = i
                reste = msg[len(commandList[i])+1:]
                break

        if commande == 0:
            try:
                self.Joueur.affiche(reste)
            except:
                print("N'est pas une voyante")

        elif commande == 1:
            self.Joueur.updateCopieJeu(reste)

Emi = Emission()
Joueur = Personnage('Alex', Emi)
Recepteur = Reception(Emi, Joueur)
Recepteur.start()