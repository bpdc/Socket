import socket
import sys
import random
import time

host = "127.0.0.1"
port = 10428

IDPROCESSO = sys.argv[1]

for i in range(0,20):
    socketvar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketvar.connect((host,port))

    valor = IDPROCESSO + " - " + "Amostra " + str(i) + " -> " + str(random.randrange(0,1000))

    print('Enviando o valor para servidor a amostra', i , valor)

    socketvar.send(bytes(valor ,"latin-1"))

    # Receve resposta dados do servidor
    dado = socketvar.recv(socket.MSG_WAITALL)

    print( dado )

    socketvar.close()

    time.sleep(2)
