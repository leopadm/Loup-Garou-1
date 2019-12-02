import socket, sys, threading, time, random

HOST = '172.16.232.50'
PORT = 8888


class ThreadClient(threading.Thread):

    def __init__(self, conn, it, role, Jeu):
        threading.Thread.__init__(self)
        self.role = role
        self.connexion = conn
        self.nom = it
        self.Jeu = Jeu
        self.connexion.send(('Vous etes bien connecte au serveur vous etes : %s\nRole : %s' % (self.nom, self.role)).encode('Utf-8'))

    def run(self):
        while True:
            msgClient = self.connexion.recv(1024).decode('Utf-8')
            self.decompose(msgClient)

    def decompose(self, msg):
        commandList = ['tue', 'protege', 'regarde']

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
            self.Jeu.regarde(reste)

    def renvoi(self, message):
        connClient[self.nom].send(message.encode('Utf-8'))

    def envoiTous(self, message):
        for cle in connClient:
            connClient[cle].send(message.encode('Utf-8'))
        print(message)

    def envoiTousSauf(self, message):
        for cle in connClient:
            if cle != self.nom:
                connClient[cle].send(message.encode('Utf-8'))
        print(message)

    def deco(self):
        self.connexion.close()
        if self.nom in connClient.keys():
            del connClient[self.nom]
        messageFin = '%s deconnecte' % self.nom
        self.envoiTous(messageFin)


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

while 1:
    connexion, adresse = mySocket.accept()

    numRole = random.randint(0, len(listeRoles)-1)

    it = 'Client-' + str(compteur)
    compteur += 1
    listeThread[it] = ThreadClient(connexion, it, listeRoles[numRole])
    print(listeRoles[numRole])
    del listeRoles[numRole]
    print(listeRoles)

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
