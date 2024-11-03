import socket
import sys

host = "127.0.0.1"
port = 10428

socketvar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketvar.connect((host,port))

while True:
    envio = input(">>> : ")
    
    # Foi digitado quit, entao finaliza o loop
    if envio.lower() == "quit":
        break

    socketvar.send(bytes(envio ,"latin-1"))

    # Receve dados do servidor
    dado = socketvar.recv(socket.MSG_WAITALL)

    # Transforma de bytes para string
    dado = dado.decode("latin-1")    

    # Foi recebido quit, entao finaliza o loop
    if dado.lower() == "quit":
        break
    
    print("<<< : ", dado )

socketvar.close()
