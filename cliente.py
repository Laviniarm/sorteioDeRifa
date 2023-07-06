import socket
import os

MAX_MESSAGE_SIZE = 1024
HOST = 'localhost'
PORT = 8888

CODIGOS_SERVIDOR = {
    '200': 'Cliente registrado com sucesso!',
    '201': 'Cliente encontrado com sucesso!',
    '202': 'Número comprado com sucesso!',
    '203': 'Números disponíveis listados.',
    '204': 'Cliente desconectado com sucesso!',
    '205': 'Rifas esgotadas.',
    '206': 'Rifas não estão esgotadas.',
    '207': 'Sorteio realizado com sucesso!',
    '208': 'Números comprados até agora.',
    '400': 'Número inválido.',
    '401': 'Número não está disponível!',
    '402': 'Ainda não é possível realizar o sorteio.'
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

    resposta = enviar_mensagem(f"REGISTRAR {input_cpf()}")
    print(CODIGOS_SERVIDOR[resposta])
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
                print(f'Números disponíveis: {resposta}')

        elif choice == '3':
            cls()
            codigo, resposta = enviar_mensagem(f"COMPRADOS").split("-", 1)
            print(CODIGOS_SERVIDOR[codigo])
            print(resposta)

        elif choice == '4':
            cls()
            resposta = enviar_mensagem(f"SORTEIO")
            if resposta == "402":
                print(CODIGOS_SERVIDOR['402'])
            else:
                _, ganhador = resposta.split("-", 1)
                numero_sorteado, cpf_ganhador = ganhador.split("-", 1)
                print(f'\nSORTEIO!\n\nNumero sorteado: {numero_sorteado}\nCPF do ganhador: {cpf_ganhador}\n')

        elif choice == '5':
            resposta = enviar_mensagem("SAIR")
            if resposta == "204":
                break

        else:
            cls()
            print("Opção inválida! Tente novamente.")

        enviar_mensagem(f"ESGOTOU")

    client_socket.close()


def comprar_rifa(enviar_mensagem):
    codigo, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
    if codigo == "203":
        print("Números disponíveis: " + resposta)
    numero = input_numero()
    if numero != '':
        codigo = enviar_mensagem(f"COMPRAR {numero}")
        print(CODIGOS_SERVIDOR[codigo])
        if codigo == "200":
            verifica_se_esgotou(enviar_mensagem(f"ESGOTOU"))
    else:
        print('Número inválido')


def input_numero():
    while True:
        numero = input("Digite o número desejado: ")
        if numero.isdigit():
            cls()
            return numero
        else:
            print("Entrada inválida. Digite apenas números.")


def input_cpf():
    cpf = input("Digite o CPF: ")
    while not valida_cpf(cpf):
        cls()
        print("CPF inválido! Tente novamente.")
        cpf = input("Digite o CPF: ")
    return cpf


def verifica_se_esgotou(resposta):
    if resposta == "205":
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
