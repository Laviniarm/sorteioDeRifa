import socket

def connect_to_server():
    # Configurando o host e a porta do servidor
    host = '192.168.0.11'  # Use o IP correto do servidor
    port = 5000

    # Criando um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectando ao servidor
    client_socket.connect((host, port))
    print(f"Conectado ao servidor {host}:{port}")

    # Lógica do cliente
    # Aqui você pode implementar a interação com o usuário para escolher um número da rifa

    # Enviando a escolha do cliente para o servidor
    client_socket.send("42".encode())

    # Recebendo a resposta do servidor
    response = client_socket.recv(1024).decode()
    print("Resposta do servidor:", response)

    # Fechando a conexão com o servidor
    client_socket.close()

connect_to_server()
