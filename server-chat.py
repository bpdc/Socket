import socket
import time
import random


host = "127.0.0.1"
port = 10428

# Cria variavel de socket
socketvar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir endereco IP e porta
socketvar.bind((host, port))

# Abrir a porta
socketvar.listen()

# Servidor fica em Loop - Todo o tempo aguardando conexao
while True:

    print("Listening on port", port)
    
    # Aguardando conexao do client
    conn, addr = socketvar.accept()
    
    # Imprime mensagem quando conectar
    print("Connected to : ", addr[0], addr[1] )

    while True:
        dado = conn.recv(socket.MSG_WAITALL) 

        # Conexao foi perdida, entao sai do loop da conexao
        if len(dado) == 0:
            print( "Disconnected")
            break

        # Transforma de bytes para string
        dado = dado.decode("latin-1")

        # Imprime o dado recebido
        print("<<< : ", dado )

        # Solicita uma palavra para responder para o client
        resposta = input(">>> : ")
        
        conn.send(bytes(resposta, "latin-1"))

    time.sleep(1)
