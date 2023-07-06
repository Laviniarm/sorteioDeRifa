import socket
import threading
from gerenciador_sorteio import Gerenciador
from lista_encadeada import ListaEncadeada

CODIGOS_SERVIDOR = {
    'OK': 200,
    'ERRO': 400
}


# Servidor com metodos de inicialização
class Server:
    def __init__(self, host, port, message_size, gerenciador: Gerenciador):
        self.__host = host
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__gerenciador = gerenciador
        self.__max_message_size = message_size
        self.__lock = threading.Lock()
        self.__clientes = ListaEncadeada()

    # Inicia o servidor
    def start(self):
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen(1)
        print(f"Servidor aguardando conexões em {self.__host}:{self.__port}")

        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

    # Trata as conexões dos clientes
    def accept_connections(self):
        while True:
            client_socket, address = self.__server_socket.accept()
            print("Cliente conectado:", address)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    # Comunicação com o cliente/ respostas para o cliente
    def handle_client(self, client_socket):
        client_socket.send("Bem-vindo à compra de rifa!".encode())
        cpf_registrado = ''

        while True:
            # Tratamento para quando o cliente desconectar
            try:
                msg_client = client_socket.recv(self.__max_message_size).decode()
            except ConnectionResetError:
                print("Cliente", client_socket.getpeername(), "desconectou!")
                break

            if msg_client.startswith("REGISTRAR"):
                cpf_registrado = self.registrar_cliente(client_socket, msg_client)

            # Compra da rifa, é adicionada na tabela o numero da rifa e cpf do comprador
            if msg_client.startswith("COMPRAR"):
                self.comprar_rifa(client_socket, cpf_registrado, msg_client)

            elif msg_client == "DISPONIVEIS":
                self.verificar_disponiveis(client_socket)

            elif msg_client == "COMPRADOS":
                client_socket.send(f"{CODIGOS_SERVIDOR['OK']}-{self.__clientes.buscar(cpf_registrado)}".encode())

            elif msg_client == "SAIR":
                self.desconectar_cliente(client_socket)
                break

            elif msg_client == "ESGOTOU":
                self.validar_esgotou(client_socket)

            elif msg_client == "SORTEIO":
                self.sortear(client_socket)

        with self.__lock:
            client_socket.close()

    def registrar_cliente(self, client_socket, msg_client):
        _, cpf = msg_client.split()
        cliente = self.__clientes.buscar(cpf)
        if cliente is None:
            self.__clientes.inserir(cpf, [])
            resposta = f"{CODIGOS_SERVIDOR['OK']}-Cliente {cpf} registrado com sucesso!"
            client_socket.send(resposta.encode())
            return cpf
        else:
            resposta = f"{CODIGOS_SERVIDOR['OK']}-Cliente {cpf} encontrado com sucesso!"
            client_socket.send(resposta.encode())
            return cpf

    def comprar_rifa(self, client_socket, cpf_registrado, msg_client):
        _, numero = msg_client.split()
        if int(numero) < 0 or int(numero) >= self.__gerenciador.get_tamanho():
            resposta = f"{CODIGOS_SERVIDOR['ERRO']}-Número inválido."
        else:
            numero_comprado = self.__gerenciador.comprar(int(numero), cpf_registrado)
            if numero_comprado > -1:
                numeros_comprados_por_cliente = self.__clientes.buscar(cpf_registrado)
                numeros_comprados_por_cliente.append(numero_comprado)
                self.__clientes.set_valor(cpf_registrado, numeros_comprados_por_cliente)
                resposta = f"{CODIGOS_SERVIDOR['OK']}-Número {numero} comprado com sucesso!"
            else:
                resposta = f"{CODIGOS_SERVIDOR['ERRO']}-Número {numero} não está disponível!"
        client_socket.send(resposta.encode())

    def verificar_disponiveis(self, client_socket):
        numeros = self.__gerenciador.numeros_nao_comprados()
        resposta = f"{CODIGOS_SERVIDOR['OK']}-Números disponíveis: " + ", ".join(map(str, numeros))
        client_socket.send(resposta.encode())

    def desconectar_cliente(self, client_socket):
        print("Cliente", client_socket.getpeername(), "desconectou!")
        enviar = f"{CODIGOS_SERVIDOR['OK']}-OFF"
        client_socket.send(enviar.encode())

    def validar_esgotou(self, client_socket):
        if self.__gerenciador.esgotou():
            enviar = f"{CODIGOS_SERVIDOR['OK']}-ESGOTOU"
            client_socket.send(enviar.encode())
        else:
            enviar = f"{CODIGOS_SERVIDOR['OK']}-NÃO ESGOTOU"
            client_socket.send(enviar.encode())

    def sortear(self, client_socket):
        if self.__gerenciador.esgotou():
            mensagem = self.__gerenciador.sorteio()
            client_socket.send(f"{CODIGOS_SERVIDOR['OK']}-{mensagem}".encode())
        else:
            enviar = f"{CODIGOS_SERVIDOR['ERRO']}-Ainda não é possível realizar o sorteio."
            client_socket.send(enviar.encode())
