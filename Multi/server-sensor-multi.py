import socket
import time
import random
from threading import Thread, Lock
import threading
from datetime import datetime

def thread_connexao(conn,addr):
    # Imprime mensagem quando conectar
    print("Connected to : ", addr[0], addr[1] )
    
    # Loop de quando o Chat foi iniciado. So sai quando o cliente desconectar
    dado = conn.recv(socket.MSG_WAITALL) 

    # Transforma de bytes para string
    dado = datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - " + dado.decode("latin-1") + "\n"

    # Append do arquivo de dados
    file1 = open("dados-client.txt", "a")  # append mode
    file1.write(dado)
    file1.close()
        
    conn.send(bytes("OK", "latin-1"))

    time.sleep(1)

    print("Finishing : ", addr[0], addr[1] )


host = "127.0.0.1"
port = 10428

# Cria variavel de socket com a opcao Multi-Theard, isto e, a para pode aceitar n clientes conectados
socketvar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketvar.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
# Definir endereco IP e porta
socketvar.bind((host, port))

# Abrir a porta
socketvar.listen(5)

# Servidor fica em Loop - Todo o tempo aguardando conexao
while True:
    print("Listening on port", port)
    
    # Aguardando conexao do client
    conn, addr = socketvar.accept()

    client_thread = threading.Thread(target=thread_connexao, args=(conn, addr))
    client_thread.start()

    time.sleep(1)
