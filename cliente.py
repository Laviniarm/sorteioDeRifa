import socket
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 8888

    client_socket.connect((host, port))

    mensagem_servidor = client_socket.recv(MAX_MESSAGE_SIZE).decode()
    print(mensagem_servidor)

    def enviar_mensagem(mensagem):
        client_socket.send(mensagem.encode())
        resposta = client_socket.recv(MAX_MESSAGE_SIZE).decode()
        return resposta

    def validaCPF(cpf):
        if len(cpf) == 11 and cpf.isdigit():
            return True
        else:
            return False

    esgotou = enviar_mensagem("ESGOTOU")

    while esgotou != "ESGOTOU":
        print('''
    1 - Comprar número
    2 - Ver números disponíveis
    3 - Ver números comprados
    4 - Sair   
    ''')
        choice = input("Digite a opção desejada: ")

        if choice == '1':
            cls()
            resposta = enviar_mensagem("NUMEROS_DISPONIVEIS")
            print(resposta)
            cpf = input("Digite o CPF: ")
            while not validaCPF(cpf):
                cls()
                print("CPF inválido! Tente novamente.")
                cpf = input("Digite o CPF: ")
            numero = input("Digite o número desejado: ")
            cls()
            resposta = enviar_mensagem(f"COMPRAR {cpf} {numero}")
            print(resposta)

            esgotou = enviar_mensagem(f"ESGOTOU")
            if esgotou == "ESGOTOU":
                while True:
                    mensagem_sorteio = client_socket.recv(1024).decode()
                    if mensagem_sorteio:
                        print(mensagem_sorteio)
                    else:
                        break                
        
        elif choice == '2':
            cls()
            resposta = enviar_mensagem("NUMEROS_DISPONIVEIS")
            print(resposta)
        
        elif choice == '3':
            cls()
            cpf = input("Digite o CPF: ")
            cls()
            resposta = enviar_mensagem(f"NUMEROS_COMPRADOS {cpf}")
            print(resposta)
        
        elif choice == '4':
            resposta = enviar_mensagem("SAIR")
            if resposta == "OFF":
                break

        else:
            cls()
            print("Opção inválida! Tente novamente.")

        esgotou = enviar_mensagem(f"ESGOTOU")

    client_socket.close()


MAX_MESSAGE_SIZE = 1024

if __name__ == '__main__':
    main()