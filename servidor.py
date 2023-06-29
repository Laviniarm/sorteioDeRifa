import socket
import threading
from TabelaHash import TabelaHash

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8888

server_socket.bind((host, port))

print(f"Servidor aguardando conexões em {host}:{port}")

# x = int(input("Quantidade de números no sorteio: "))
tabela = TabelaHash(3)
clientes = []

def handle_client(client_socket):
    clientes.append(client_socket)
    print("Cliente conectado:", client_socket.getpeername())
    
    mensagem = "Bem vindo à compra de rifa!"
    client_socket.send(mensagem.encode())
    
    while True:
        try:
            msg_client = client_socket.recv(1024).decode()
        except ConnectionResetError:
            break

        if msg_client.startswith("COMPRAR"):
            _, cpf, numero = msg_client.split()
            if int(numero) < 0 or int(numero) >= len(tabela):
                resposta = 'Número inválido.'
            else:
                numero_comprado = tabela.comprar(int(numero), cpf)
                if numero_comprado:
                    resposta = f'Número {numero} comprado com sucesso!'
                else:
                    resposta = f'Número {numero} não está disponível!'
            client_socket.send(resposta.encode())
        
        elif msg_client == "NUMEROS_DISPONIVEIS":
            numeros = tabela.numeros_nao_comprados()
            resposta = "Números disponíveis: " + ", ".join(map(str, numeros))
            client_socket.send(resposta.encode())

        elif msg_client.startswith("NUMEROS_COMPRADOS"):
            _, valor = msg_client.split()
            resposta = tabela.imprimirCPF(valor)
            client_socket.send(resposta.encode())
        
        # elif msg_client == "SORTEAR":
        #     resposta = tabela.sorteio()
        #     client_socket.send(resposta.encode())
        
        elif msg_client == "SAIR":
            break
        
        elif msg_client == "ESGOTOU":
            if tabela.esgotou():
                enviar = "ESGOTOU"
                client_socket.send(enviar.encode())
            else:
                enviar = "NÃO ESGOTOU"
                client_socket.send(enviar.encode())

        elif msg_client == "SORTEIO":
            mensagem = tabela.sorteio()
            for cliente in clientes[:]:
                cliente.send(mensagem.encode())

       # elif msg_client == "SORTEIO":
        #    mensagem = tabela.sorteio()
        #    client_socket.send(mensagem.encode())

def accept_connections():
    while True:
        server_socket.listen(1)
        print("Aguardando conexões...")

        client_socket, address = server_socket.accept()
        print("Cliente conectado:", address)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()