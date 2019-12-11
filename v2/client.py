from threading import Thread
import socket, sys
from v2.Personnage import Personnage

class Emission(object):

    def __init__(self, HOST="192.168.1.20", PORT=8888):
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = HOST
        self.PORT = PORT

        try:
            self.connexion.connect((self.HOST, self.PORT))
            print('Connecte au serveur')
        except socket.error:
            print('La liaison a echoue')
            sys.exit()


    def envoi(self, colis):
        self.connexion.send(colis.encode('Utf-8'))

    def fermerConnexion(self):
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
        self.running = True
        while self.running:
            try:
                msgRecu = self.connexion.recv(1024).decode('Utf-8')
                print(msgRecu)
                if msgRecu.upper() == 'FIN':
                    self.connexion.send('FIN'.encode('Utf-8'))
                    self.stopThread()
                    break
            except:
                self.Emetteur.fermerConnexion()
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

    def stopThread(self):
        self.running = False

Emi = Emission()
Joueur = Personnage('Alex', Emi)
Recepteur = Reception(Emi, Joueur)
Recepteur.start()