import socket

# Definir o host e a porta para o servidor
host = 'localhost'  # substitua pelo endereço IP ou hostname do servidor
port = 1024

# Criar um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permitir reuso do endereço
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Vincular o socket ao host e porta
sock.bind((host, port))

# Ouvir por conexões entrantes
sock.listen(1)

print("Servidor aguardando conexões na porta", port)

while True:
    # Aguardar por uma nova conexão
    client_socket, client_address = sock.accept()

    print("Conexão estabelecida a partir de:", client_address)

    # Receber os dados enviados pelo cliente
    data = client_socket.recv(1024).decode()
    while data:
        print("Mensagem recebida do cliente:", data)

        # Enviar uma resposta de volta ao cliente
        resposta = "Olá, cliente!"
        client_socket.sendall(resposta.encode())

        # Receber mais dados do cliente
        data = client_socket.recv(1024).decode()

    # Fechar a conexão com o cliente
    client_socket.close()