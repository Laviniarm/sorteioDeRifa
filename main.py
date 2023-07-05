from servidor_teste import Server
from gerenciador_sorteio import Gerenciador

MESSAGE_SIZE = 1024
HOST = 'localhost'
PORT = 8888
gerenciador = None

try:
    quantidade = int(input("Quantidade de números no sorteio: "))
    if quantidade > 0:
        gerenciador = Gerenciador(quantidade)
    else:
        print("A quantidade deve ser um número inteiro positivo.")
except ValueError:
    print("A quantidade deve ser um número inteiro positivo.")

if gerenciador is not None:
    server = Server(HOST, PORT, MESSAGE_SIZE, gerenciador)
    server.start()
