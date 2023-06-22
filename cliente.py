import socket
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8888

client_socket.connect((host, port))

mensagem_servidor = client_socket.recv(1024).decode()
print("Mensagem do servidor:", mensagem_servidor)

def enviar_mensagem(mensagem):
    client_socket.send(mensagem.encode())
    resposta = client_socket.recv(1024).decode()
    return resposta

while True:
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

client_socket.close()