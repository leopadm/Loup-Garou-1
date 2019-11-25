import socket, sys, threading, time

HOST = '172.16.230.184'
PORT = 8888


class ThreadClient(threading.Thread):

    def __init__(self, conn, it):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.nom = it
        msgAccueil = 'Vous etes bien connecte au serveur vous etes : %s' % self.nom
        self.connexion.send(msgAccueil.encode('Utf-8'))

    def run(self):
        while True:
            msgClient = self.connexion.recv(1024).decode('Utf-8')

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
while 1:
    connexion, adresse = mySocket.accept()

    it = 'Client-' + str(compteur)
    compteur += 1
    listeThread[it] = ThreadClient(connexion, it)
    listeThread[it].start()
    connClient[it] = connexion

    msgConnexion = "%s connecte, adresse IP %s , port %s" % (it, adresse[0], adresse[1])
    print(msgConnexion)
    try:
        for cle in connClient.keys():
            if cle != it:
                connClient[cle].send(msgConnexion.encode('Utf-8'))
    except ConnectionResetError:
        print('')

    msgAccueil = 'Vous etes bien connecte au serveur vous etes : %s' % it
    connexion.send(msgAccueil.encode('Utf-8'))
