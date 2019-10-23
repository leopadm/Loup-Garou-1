import socket, sys, threading, time


class ThreadReception(threading.Thread):

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            msgRecu = self.connexion.recv(1024).decode('Utf-8')
            if not msgRecu or msgRecu.upper() == 'FIN':
                self.connexion.send('FIN'.encode('Utf-8'))
                break
            print(msgRecu)
        print('Connexion interrompue')
        self.connexion.close()


class ThreadEmission(threading.Thread):

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            msgEmis = input()
            self.connexion.send(msgEmis.encode('Utf-8'))


class ClientVillage(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.HOST = '172.16.236.77'
        self.PORT = 5000

    def run(self):

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            connexion.connect((self.HOST, self.PORT))
        except socket.error:
            print('La liaison a echoue')
            sys.exit()
        print('Connecte au serveur')

        th_E = ThreadEmission(connexion)
        th_R = ThreadReception(connexion)
        th_E.start()
        th_R.start()
