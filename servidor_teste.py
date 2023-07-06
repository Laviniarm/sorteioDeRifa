import socket
import threading
from gerenciador import Gerenciador
import gerenciador_servidor


# Servidor com metodos de inicialização
class Server:
    def __init__(self, host, port, message_size, gerenciador: Gerenciador):
        self._host = host
        self._port = port
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._gerenciador = gerenciador
        self._max_message_size = message_size
        self._lock = threading.Lock()
        self._clientes = ListaEncadeada()

    # Inicia o servidor
    def start(self):
        self._server_socket.bind((self._host, self._port))
        self._server_socket.listen(1)
        print(f"Servidor aguardando conexões em {self._host}:{self._port}")

        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

    # Trata as conexões dos clientes
    def accept_connections(self):
        while True:
            client_socket, address = self._server_socket.accept()
            print("Cliente conectado:", address)
            self._clientes.inserir(address, [])

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    # Comunicação com o cliente/ respostas para o cliente
    def handle_client(self, client_socket):
        mensagem = "Bem-vindo à compra de rifa!"
        client_name = client_socket.getpeername()[1]
        client_socket.send(mensagem.encode())

        while True:
            # Tratamento para quando o cliente desconectar
            try:
                msg_client = client_socket.recv(self._max_message_size).decode()
            except ConnectionResetError:
                print("Cliente", client_socket.getpeername(), "desconectou!")
                break

            # Compra da rifa, é adicionada na tabela o numero da rifa e cpf do comprador
            if msg_client.startswith("COMPRAR"):
                _, cpf, numero = msg_client.split()
                if int(numero) < 0 or int(numero) >= self._gerenciador.get_tamanho():
                    resposta = 'Número inválido.'
                else:
                    numero_comprado = self._gerenciador.comprar(int(numero), cpf)
                    if numero_comprado > 0:
                        numeros_comprados_por_cliente = self._clientes.buscar(client_name)
                        numeros_comprados_por_cliente.append(numero_comprado)
                        self._clientes.setValor(client_name, numeros_comprados_por_cliente)
                        resposta = f'Número {numero} comprado com sucesso!'
                    else:
                        resposta = f'Número {numero} não está disponível!'
                client_socket.send(resposta.encode())

            elif msg_client == "DISPONIVEIS":
                numeros = self._gerenciador.numeros_nao_comprados()
                resposta = "Números disponíveis: " + ", ".join(map(str, numeros))
                client_socket.send(resposta.encode())

            elif msg_client.startswith("COMPRADOS"):
                _, valor = msg_client.split()
                resposta = self._gerenciador.imprimir_cpf(valor)
                client_socket.send(resposta.encode())

            elif msg_client == "SAIR":
                print("Cliente", client_socket.getpeername(), "desconectou!")
                enviar = "OFF"
                client_socket.send(enviar.encode())
                break

            elif msg_client == "ESGOTOU":
                if self._gerenciador.esgotou():
                    enviar = "ESGOTOU"
                    client_socket.send(enviar.encode())
                else:
                    enviar = "NÃO ESGOTOU"
                    client_socket.send(enviar.encode())

            elif msg_client == "SORTEIO":
                if self._gerenciador.esgotou():
                    mensagem = self._gerenciador.sorteio()
                    client_socket.send(mensagem.encode())
                else:
                    enviar = "Ainda não é possível realizar o sorteio."
                    client_socket.send(enviar.encode())

            elif msg_client == "CLIENTE_COMPRADOS":
                numeros_comprados_por_cliente = self._clientes.buscar(client_name)
                client_socket.send(f'{numeros_comprados_por_cliente}'.encode())

        with self._lock:
            client_socket.close()

