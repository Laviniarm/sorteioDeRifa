import socket
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8888

client_socket.connect((host, port))

mensagem_servidor = client_socket.recv(1024).decode()
print(mensagem_servidor)

def enviar_mensagem(mensagem):
    client_socket.send(mensagem.encode())
    resposta = client_socket.recv(1024).decode()
    return resposta

def validaCPF(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        return True
    else:
        return False

esgotou = enviar_mensagem(f"ESGOTOU")

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
        break

    else:
        cls()
        print("Opção inválida! Tente novamente.")

    esgotou = enviar_mensagem(f"ESGOTOU")

sorteio = enviar_mensagem(f"SORTEIO")
print(sorteio)

x = input("Para encerrar digite 0: ")
if x == 0:
    client_socket.close()