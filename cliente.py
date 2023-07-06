import socket
import os

MAX_MESSAGE_SIZE = 1024
HOST = 'localhost'
PORT = 8888
CODIGOS_SERVIDOR = {
    '200': 'Operação realizada com sucesso',
    '400': 'Operação não disponível'
}


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

    enviar_mensagem(f"REGISTRAR {input_cpf()}")

    resposta = enviar_mensagem("ESGOTOU")

    verifica_se_esgotou(resposta)

    while True:
        choice = mostrar_menu()

        if choice == '1':
            cls()
            if not verifica_se_esgotou(enviar_mensagem("ESGOTOU")):
                comprar_rifa(enviar_mensagem)

        elif choice == '2':
            cls()
            if not verifica_se_esgotou(enviar_mensagem("ESGOTOU")):
                _, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
                print(resposta)

        elif choice == '3':
            cls()
            _, resposta = enviar_mensagem(f"COMPRADOS").split("-", 1)
            print(resposta)

        elif choice == '4':
            cls()
            codigo, resposta = enviar_mensagem(f"SORTEIO").split("-", 1)
            print(CODIGOS_SERVIDOR[codigo])
            print(resposta)

        elif choice == '5':
            _, resposta = enviar_mensagem("SAIR").split("-", 1)
            if resposta == "OFF":
                break

        else:
            cls()
            print("Opção inválida! Tente novamente.")

        enviar_mensagem(f"ESGOTOU")

    client_socket.close()


def comprar_rifa(enviar_mensagem):
    _, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
    print(resposta)
    numero = input_numero()
    if numero != '':
        codigo, resposta = enviar_mensagem(f"COMPRAR {numero}").split("-", 1)
        print(CODIGOS_SERVIDOR[codigo])
        if codigo == 200:
            print(resposta)
            verifica_se_esgotou(enviar_mensagem(f"ESGOTOU"))
    else:
        print('Número inválido')


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
    _, resposta = resposta.split("-", 1)
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
    5 - Sair  
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
