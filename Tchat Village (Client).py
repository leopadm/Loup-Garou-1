import socket, sys, threading, time

HOST = '172.16.230.224'
PORT = 5000
LOG = ""


class ThreadReception(threading.Thread):

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        global LOG
        while 1:
            msgRecu = self.connexion.recv(1024).decode('Utf-8')
            LOG = LOG + msgRecu + '\n'
            if not msgRecu or msgRecu.upper() == 'FIN':
                self.connexion.send('FIN'.encode('Utf-8'))
                break
            print(msgRecu)
        th_E._stop()
        print('Connexion interrompue')
        self.connexion.close()


class ThreadEmission(threading.Thread):

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        global LOG
        while 1:
            msgEmis = input()
            self.connexion.send(msgEmis.encode('Utf-8'))
            LOG = LOG + 'Moi -> ' + msgEmis + '\n'
            print(LOG)


connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    connexion.connect((HOST, PORT))
except socket.error:
    print('La liaison a echoue')
    sys.exit()
print('Connecte au serveur')

th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()
