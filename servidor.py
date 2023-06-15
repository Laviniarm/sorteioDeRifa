import socket
import threading


def realizar_login(client_socket):
    # Implemente a lógica de login do servidor
    pass

def realizar_registro(client_socket):
    # Implemente a lógica de registro do servidor
    pass

def enviar_numeros_disponiveis(client_socket):
    # Implemente a lógica para enviar ao cliente a lista de números disponíveis
    pass

def comprar_numero(client_socket, numero):
    # Implemente a lógica para registrar a compra de um número específico pelo cliente
    pass

def sortear_numero():
    # Implemente a lógica para realizar o sorteio do número vencedor
    pass

def enviar_resultado_sorteio(client_socket):
    # Implemente a lógica para enviar ao cliente o resultado do sorteio
    pass


def handle_client(client_socket):
    while True:
        # Receber a mensagem do cliente
        data = client_socket.recv(1024).decode()
        if not data:
            break

        # Interpretar a mensagem recebida e chamar a função correspondente
        command, *args = data.split()
        if command == "LOGIN":
            realizar_login(client_socket)
        elif command == "REGISTRO":
            realizar_registro(client_socket)
        elif command == "EXIBIR":
            enviar_numeros_disponiveis(client_socket)
        elif command == "COMPRAR":
            numero = args[0]
            comprar_numero(client_socket, numero)
        elif command == "SORTEIO":
            sortear_numero()
            enviar_resultado_sorteio(client_socket)

    # Fechar a conexão com o cliente
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