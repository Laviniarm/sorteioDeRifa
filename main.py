import sys
from servidor import Server
from gerenciador_sorteio import Gerenciador

MESSAGE_SIZE = 1024
HOST = '0.0.0.0'
PORT = 8888
gerenciador = None

if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

def input_quantidade():
    while True:
        numero = input("Quantidade de números no sorteio: ")
        if numero.isdigit():
            return numero
        else:
            print("Entrada inválida. Digite apenas números.")

'''
Classe responsável por iniciar o servidor
'''
try:
    quantidade = int(input_quantidade())
    if quantidade > 0:
        gerenciador = Gerenciador(quantidade)
    else:
        print("A quantidade deve ser um número inteiro positivo.")
except ValueError:
    print("A quantidade deve ser um número inteiro positivo.")

if gerenciador is not None:
    server = Server(HOST, PORT, MESSAGE_SIZE, gerenciador)
    server.start()