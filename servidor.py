import socket
import threading

def handle_client(client_socket):
    # Lógica para tratar as requisições do cliente
    # Aqui você pode implementar a lógica do sorteio da rifa

    # Exemplo de envio de uma mensagem de resposta para o cliente
    response = "O número sorteado é: 42"
    client_socket.send(response.encode())

    # Fechando a conexão com o cliente
    client_socket.close()

def start_server():
    # Configurando o host e a porta do servidor
    host = '192.168.0.11'  # Use o IP correto do servidor
    port = 5000

    # Criando um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ligando o socket ao host e à porta
    server_socket.bind((host, port))

    # Habilitando o servidor para aceitar conexões
    server_socket.listen(5)
    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        # Aceitando a conexão de um cliente
        client_socket, address = server_socket.accept()
        print(f"Conexão estabelecida com {address[0]}:{address[1]}")

        # Criando uma nova thread para tratar o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()