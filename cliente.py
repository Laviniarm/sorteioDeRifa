import socket


def realizar_login():
    # Implemente a lógica de login do cliente
    print("Realizando login do cliente...")


def realizar_registro():
    # Implemente a lógica de registro do cliente
    print("Realizando registro do cliente...")


def exibir_numeros_disponiveis():
    # Implemente a lógica para solicitar ao servidor a lista de números disponíveis
    print("Exibindo números disponíveis...")


def comprar_numero(numero):
    # Implemente a lógica para solicitar ao servidor a compra de um número específico
    print("Comprando número:", numero)


def consultar_resultado():
    # Implemente a lógica para solicitar ao servidor o resultado do sorteio
    print("Consultando resultado do sorteio...")


def exibir_menu():
    while True:
        print("== Menu ==")
        print("1. Login")
        print("2. Registro")
        print("3. Exibir números disponíveis")
        print("4. Comprar número")
        print("5. Consultar resultado do sorteio")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            realizar_login()
        elif opcao == "2":
            realizar_registro()
        elif opcao == "3":
            exibir_numeros_disponiveis()
        elif opcao == "4":
            numero = input("Digite o número que deseja comprar: ")
            comprar_numero(numero)
        elif opcao == "5":
            consultar_resultado()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

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
    exibir_menu()
    # Aqui você pode implementar a interação com o usuário para escolher um número da rifa

    # Enviando a escolha do cliente para o servidor
    numero_escolhido = "42"
    client_socket.send(numero_escolhido.encode())
    # Recebendo a resposta do servidor
    response = client_socket.recv(1024).decode()
    print("Resposta do servidor:", response)

    # Fechando a conexão com o servidor
    client_socket.close()

connect_to_server()
