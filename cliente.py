import socket
import os

MAX_MESSAGE_SIZE = 1024
HOST = 'localhost'
PORT = 8888


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    mensagem_servidor = client_socket.recv(MAX_MESSAGE_SIZE).decode()
    print(mensagem_servidor)

    def enviar_mensagem(mensagem):
        client_socket.send(mensagem.encode())
        return client_socket.recv(MAX_MESSAGE_SIZE).decode()

    resposta = enviar_mensagem("ESGOTOU")

    verifica_se_esgotou(resposta)

    while True:
        choice = mostrar_menu()

        if choice == '1':
            cls()
            resposta = enviar_mensagem("DISPONIVEIS")
            if not verifica_se_esgotou(resposta):
                print(resposta)
                resposta = enviar_mensagem(f"COMPRAR {input_cpf()} {input_numero()}")
                print(resposta)
                verifica_se_esgotou(enviar_mensagem(f"ESGOTOU"))

        elif choice == '2':
            cls()
            resposta = enviar_mensagem("DISPONIVEIS")
            if not verifica_se_esgotou(resposta):
                resposta = enviar_mensagem("DISPONIVEIS")
                print(resposta)

        elif choice == '3':
            cls()
            cpf = input("Digite o CPF: ")
            cls()
            resposta = enviar_mensagem(f"COMPRADOS {cpf}")
            print(resposta)

        elif choice == '4':
            cls()
            resposta = enviar_mensagem(f"SORTEIO")
            print(resposta)

        elif choice == '5':
            cls()
            resposta = enviar_mensagem(f"CLIENTE_COMPRADOS")
            print(resposta)

        elif choice == '6':
            resposta = enviar_mensagem("SAIR")
            if resposta == "OFF":
                break

        else:
            cls()
            print("Opção inválida! Tente novamente.")

        enviar_mensagem(f"ESGOTOU")

    client_socket.close()


def input_numero():
    numero = input("Digite o número desejado: ")
    cls()
    return numero


def input_cpf():
    cpf = input("Digite o CPF: ")
    while not valida_cpf(cpf):
        cls()
        print("CPF inválido! Tente novamente.")
        cpf = input("Digite o CPF: ")
    return cpf


def verifica_se_esgotou(resposta):
    if resposta == "ESGOTOU":
        print("Numeros esgotados, o sorteio já pode ser realizado")
        return True
    else:
        return False


def mostrar_menu():
    print('''
    1 - Comprar número
    2 - Ver números disponíveis
    3 - Ver números comprados
    4 - Sorteio
    5 - Ver todos os números comprados neste cliente
    6 - Sair  
    ''')
    choice = input("Digite a opção desejada: ")
    return choice


def valida_cpf(_cpf):
    if len(_cpf) == 11 and _cpf.isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    main()
