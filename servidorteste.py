import socket
import threading
from TabelaHash import TabelaHash

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tabela = None
        self.clientes = []
        self.max_message_size = 1024
        self.lock = threading.Lock()

    def obter_quantidade_tabela(self):
        while True:
            try:
                quantidade = int(input("Quantidade de números no sorteio: "))
                if quantidade > 0:
                    return TabelaHash(quantidade)
                else:
                    print("A quantidade deve ser um número inteiro positivo.")
            except ValueError:
                print("A quantidade deve ser um número inteiro positivo.")

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Servidor aguardando conexões em {self.host}:{self.port}")
        
        try:
            self.tabela = self.obter_quantidade_tabela()
        except Exception as e:
            print("Erro ao obter a tabela hash:", str(e))
            return
        
        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

    def accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print("Cliente conectado:", address)

            self.clientes.append(client_socket)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        self.clientes.append(client_socket)
        print("Cliente conectado:", client_socket.getpeername())

        mensagem = "Bem-vindo à compra de rifa!"
        client_socket.send(mensagem.encode())

        while True:
            try:
                msg_client = client_socket.recv(1024).decode()
            except ConnectionResetError:
                print("Cliente", client_socket.getpeername(), "desconectou!")
                break

            if msg_client.startswith("COMPRAR"):
                _, cpf, numero = msg_client.split()
                if int(numero) < 0 or int(numero) >= len(self.tabela):
                    resposta = 'Número inválido.'
                else:
                    numero_comprado = self.tabela.comprar(int(numero), cpf)
                    if numero_comprado:
                        resposta = f'Número {numero} comprado com sucesso!'
                    else:
                        resposta = f'Número {numero} não está disponível!'
                client_socket.send(resposta.encode())

            elif msg_client == "NUMEROS_DISPONIVEIS":
                numeros = self.tabela.numeros_nao_comprados()
                resposta = "Números disponíveis: " + ", ".join(map(str, numeros))
                client_socket.send(resposta.encode())

            elif msg_client.startswith("NUMEROS_COMPRADOS"):
                _, valor = msg_client.split()
                resposta = self.tabela.imprimirCPF(valor)
                client_socket.send(resposta.encode())

            elif msg_client == "SAIR":
                print("Cliente", client_socket.getpeername(), "desconectou!")
                enviar = "OFF"
                client_socket.send(enviar.encode())
                break

            elif msg_client == "ESGOTOU":
                if self.tabela.esgotou():
                    enviar = "ESGOTOU"
                    client_socket.send(enviar.encode())
                else:
                    enviar = "NÃO ESGOTOU"
                    client_socket.send(enviar.encode())

            elif msg_client == "SORTEIO":
                if self.tabela.esgotou():
                    mensagem = self.tabela.sorteio()
                    with self.lock:
                        for cliente in self.clientes:
                            cliente.send(mensagem.encode())
                    break
                else:
                    enviar = "Ainda não é possível realizar o sorteio."
                    client_socket.send(enviar.encode())

            # elif msg_client == "SORTEIO":
            #    mensagem = tabela.sorteio()
            #    client_socket.send(mensagem.encode())

        with self.lock:
            self.clientes.remove(client_socket)
            client_socket.close()


host = 'localhost'
port = 8888


server = Server(host, port)
server.start()
