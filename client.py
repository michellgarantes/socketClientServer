import socket

# Definir o host e a porta do servidor
host = 'localhost'  # substitua pelo endereço IP ou hostname do servidor
port = 1024

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar ao servidor
    sock.connect((host, port))
    print("Conexão estabelecida com o servidor.")

    # Enviar dados para o servidor
    while True:
        mensagem = input()
        sock.sendall(mensagem.encode())
        if mensagem == 0:
            break
        
    
    # Receber e imprimir a resposta do servidor
    resposta = sock.recv(1024).decode()
    print("Resposta do servidor:", resposta)

finally:
    # Fechar a conexão
    sock.close()
