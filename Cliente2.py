import socket

def realizar_registro(client_socket):
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    mensagem = f"REGISTRO|{nome}|{cpf}"
    client_socket.send(mensagem.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def comprar_numero(client_socket):
    numero = input("Digite o número que deseja comprar: ")
    mensagem = f"COMPRA|{numero}"
    client_socket.send(mensagem.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def exibir_numeros_disponiveis(client_socket):
    mensagem = "NUMEROS_DISPONIVEIS"
    client_socket.send(mensagem.encode())
    response = client_socket.recv(1024).decode()
    print("Números disponíveis:", response)

def consultar_resultado(client_socket):
    mensagem = "CONSULTAR_RESULTADO"
    client_socket.send(mensagem.encode())
    response = client_socket.recv(1024).decode()
    print("Resultado do sorteio:", response)

def connect_to_server():
    host = '192.168.0.11'  # IP do servidor
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Conectado ao servidor {host}:{port}")

    while True:
        print("== Menu ==")
        print("1. Registro")
        print("2. Comprar número")
        print("3. Exibir números disponíveis")
        print("4. Consultar resultado do sorteio")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            realizar_registro(client_socket)
        elif opcao == "2":
            comprar_numero(client_socket)
        elif opcao == "3":
            exibir_numeros_disponiveis(client_socket)
        elif opcao == "4":
            consultar_resultado(client_socket)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    client_socket.close()

connect_to_server()