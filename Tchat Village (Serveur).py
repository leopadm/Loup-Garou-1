import socket, sys, threading, time

HOST = '172.16.230.224'
PORT = 5000

class ThreadClient(threading.Thread):

    def __init__(self, conn, it):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.nom = it

    def run(self):
        while 1:
            msgClient = self.connexion.recv(1024).decode('Utf-8')
            if not msgClient or msgClient.upper() == 'FIN':
                break
            elif msgClient[0] == '!':
                self.special(msgClient)
            if msgClient[0] != '!':
                message = "%s> %s" % (self.nom, msgClient)
                self.envoiTousSauf(message)
        self.deco()

    def special(self, msg):
        global connClient
        global listeThread
        commandList = ['!ban ', '!changeName ', '!commands', '!time']
        decription = "Liste des commandes:\n" \
                     "!ban + pseudo          Banni la personne dont le pseudo est indique\n" \
                     "!changeName + pseudo   Change son nom par le pseudo\n" \
                     "!commands              Indique la liste des commandes disponnibles\n" \
                     "!time                  Donne l'heure"
        choix = -1
        for i in range(len(commandList)):
            if msg[0:][:len(commandList[i])] == commandList[i]:
                choix = i
                break
        #fonctions des commandes
        if choix != -1:

            # Commande : '!ban '
            if choix == 0:
                pseudo = msg[len(commandList[0]):]
                if pseudo in listeThread.keys() and pseudo != self.nom:
                    connClient[pseudo].send('FIN'.encode('Utf-8'))
                    del connClient[pseudo]
                    self.envoiTous('%s a ete banni' % pseudo)
                else:
                    self.renvoi("%s n'existe pas" % pseudo)

            # Commande : '!changeName '
            elif choix == 1:
                nouveauNom = msg[len(commandList[1]):]
                if nouveauNom not in connClient.keys():
                    connClient[nouveauNom] = connClient.pop(self.nom)
                    listeThread[nouveauNom] = listeThread.pop(self.nom)
                    ancien = self.nom
                    self.nom = nouveauNom
                    self.envoiTous("%s s'appelle desormais %s" % (ancien, nouveauNom))
                else:
                    self.renvoi('%s est deja pris par un utilisateur' % nouveauNom)

            # Commande : '!commands'
            elif choix == 2 and len(msg) == len(commandList[2]):
                self.renvoi(decription)

            # Commande : '!time'
            elif choix == 3 and len(msg) == len(commandList[3]):
                self.renvoi('Il est actuellement '+ time.strftime("%H:%M:%S"))
        else:
            self.renvoi('Commande Inconnue')

    def renvoi(self, message):
            connClient[self.nom].send(message.encode('Utf-8'))

    def envoiTous(self, message):
        print(message)
        for cle in connClient:
            connClient[cle].send(message.encode('Utf-8'))

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
    print('Connexion non etablie')
    sys.exit()
print('Serveur pret...')

mySocket.listen(5)

connClient = {}
listeThread = {}
compteur = 1
while 1:
    connexion, adresse = mySocket.accept()

    it = 'Client-' + str(compteur)
    compteur += 1
    listeThread[it] = ThreadClient(connexion, it)
    listeThread[it].start()
    connClient[it] = connexion

    msgConnexion = "%s connecte, adresse IP %s , port %s" % (it, adresse[0], adresse[1])
    print(msgConnexion)
    for cle in connClient:
        if cle != it:
            connClient[cle].send(msgConnexion.encode('Utf-8'))
    msgAccueil = 'Vous etes connecte au serveur de chat vous etes : %s' % it
    connexion.send(msgAccueil.encode('Utf-8'))