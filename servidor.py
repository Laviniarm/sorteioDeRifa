import socket
import threading
from TabelaHash import TabelaHash
from Rifa import Rifa
from Pessoa import Pessoa

def handle_registro(client_socket, tabela_hash):
    data = client_socket.recv(1024).decode()
    nome, cpf = data.split("|")[1:]
    Pessoa(nome, cpf)
    response = "Registro realizado com sucesso."
    client_socket.send(response.encode())

def handle_compra(client_socket, tabela_hash, rifa):
    data = client_socket.recv(1024).decode()
    cpf, numero = data.split("|")[1:]
    
    # Verificar se o CPF está registrado na tabela hash
    if tabela_hash.buscar(cpf) is None:
        response = "CPF não registrado. Realize o registro antes de efetuar a compra."
        client_socket.send(response.encode())
        return
    
    # Verificar se o número da rifa está disponível
    if numero not in rifa.numeros_disponiveis:
        response = "Número da rifa indisponível. Escolha outro número."
        client_socket.send(response.encode())
        return
    
    # Realizar a compra do número pela pessoa correspondente
    pessoa = tabela_hash.buscar(cpf)
    pessoa.comprar_numero(numero, tabela_hash)
    rifa.numeros_disponiveis.remove(numero)
    
    response = "Compra realizada com sucesso."
    client_socket.send(response.encode())

def handle_numeros_disponiveis(client_socket, rifa):
    numeros_disponiveis = rifa.numeros_disponiveis
    response = ",".join(map(str, numeros_disponiveis))
    client_socket.send(response.encode())

def handle_consultar_resultado(client_socket, rifa):
    try:
        numero_sorteado = rifa.sortear_numero()
        response = str(numero_sorteado)
    except ValueError as e:
        response = str(e)
    client_socket.send(response.encode())

def handle_client(client_socket, client_address, tabela_hash, rifa):
    print(f"Conexão estabelecida com {client_address[0]}:{client_address[1]}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        if data.startswith("REGISTRO"):
            handle_registro(client_socket, tabela_hash)
        elif data.startswith("COMPRA"):
            handle_compra(client_socket, tabela_hash)
        elif data == "NUMEROS_DISPONIVEIS":
            handle_numeros_disponiveis(client_socket, rifa)
        elif data == "CONSULTAR_RESULTADO":
            handle_consultar_resultado(client_socket, rifa)

    client_socket.close()
    print(f"Conexão encerrada com {client_address[0]}:{client_address[1]}")

def start_server():
    host = '192.168.0.11'  # IP do servidor
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor aguardando conexões em {host}:{port}")

    rifa = Rifa()
    rifa.criar_lista()

    tabela_hash = TabelaHash(31)

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, tabela_hash, rifa))
        client_thread.start()

start_server()
