import socket, sys, threading, random
from v2.Jeu import Jeu

HOST = '192.168.1.20'
PORT = 8888


class ThreadClient(threading.Thread):

    def __init__(self, conn, it, role, Jeu):
        threading.Thread.__init__(self)
        self.role = role
        self.connexion = conn
        self.nom = it
        # Jeu est bien ici l'objet du village
        self.Jeu = Jeu
        msgVerif = 'Vous etes bien connecte au serveur vous etes : %s\nRole : %s' % (self.nom, self.role)
        self.connexion.send(msgVerif.encode('Utf-8'))

    def run(self):
        self.running = True
        while (self.running):
            try:
                msgClient = self.connexion.recv(1024).decode('Utf-8')
                print(msgClient)
                self.decompose(msgClient)
            except:
                self.deco()

    def decompose(self, msg):
        commandList = ['tue', 'protege', 'regarde']

        # Formats demmandes:
        #     tue:          "tue [pseudo]"           => returns :  True ou False
        #     protege :     "protege [pseudo]"       => returns :  True ou False
        #     regarde :     "regarde [pseudo]"       => returns :  "rregarde %s' % role"

        commande = -1
        reste = ''
        for i in range(len(commandList)):
            if msg[0:][:len(commandList[i])] == commandList[i]:
                commande = i
                reste = msg[len(commandList[i])+1:]
                print('Commande : %s >> %s' % (commande, reste))
                break

        if commande == 1:
            self.Jeu.tue(reste)

        elif commande == 2:
            self.Jeu.protege(reste)

        elif commande == 3:
            self.renvoi(self.Jeu.regarde(reste).encode('Utf-8'))

        else:
            print('Message dans un format non compatible')

    def renvoi(self, message):
        try:
            connClient[self.nom].send(message.encode('Utf-8'))
            print(connClient[self.nom])
        except:
            print("Erreur de connexion 1")
            self.deco()

    def envoiTous(self, message):
        try:
            for cle in connClient:
                connClient[cle].send(message.encode('Utf-8'))
            print(message)
        except:
            print("Erreur de connexion 2")
            self.deco()

    def envoiTousSauf(self, message):
        try:
            for cle in connClient:
                if cle != self.nom:
                    connClient[cle].send(message.encode('Utf-8'))
            print(message)
        except:
            print("Erreur de connexion 3")
            self.deco()

    def deco(self):
        try:
            if self.nom in connClient.keys():
                del connClient[self.nom]
            messageFin = '%s deconnecte' % self.nom
            self.envoiTous(messageFin)
            self.connexion.close()
        finally:
            self.stopThread()

    def stopThread(self):
        self.running = False

LeJeu = Jeu()

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("Connexion non etablie, verifiez l'adresse IP de l'hote")
    sys.exit()
print('Serveur pret...')

mySocket.listen(5)

connClient = {}
listeThread = {}
compteur = 1

listeRoles = ['loup', 'loup', 'sorciere', 'chaman', 'voyante', 'salvateur', 'chasseur' ]

while True:
    connexion, adresse = mySocket.accept()

    numRole = random.randint(0, len(listeRoles)-1)

    it = 'Client-' + str(compteur)
    compteur += 1
    listeThread[it] = ThreadClient(connexion, it, listeRoles[numRole], LeJeu)
    del listeRoles[numRole]

    listeThread[it].start()
    connClient[it] = connexion

    msgConnexion = "%s connecte, adresse IP %s , port %s" % (it, adresse[0], adresse[1])
    print(msgConnexion)
    try:
        for cle in connClient.keys():
            if cle != it:
                connClient[cle].send(msgConnexion.encode('Utf-8'))
    except ConnectionResetError:
        print('ERREUR CONNEXION')
