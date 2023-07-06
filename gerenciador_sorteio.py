import random
from TabelaHash import TabelaHash


class Gerenciador:

    def __init__(self, tamanho):
        self._tabela_rifa = TabelaHash(tamanho)
        self._comprados = {}
        self._numero_sorteado = None
        self._cpf_sorteado = None

    def comprar(self, numero, cpf):
        self._comprados[numero] = cpf
        return self._tabela_rifa.put(numero, cpf)
    
    def numeros_nao_comprados(self):
        return self._tabela_rifa.get_valores_vazios()
   
    def sorteio(self):
        if self._numero_sorteado is None:
            cpf, numero_sorteado = self.realizar_sorteio()
            self._numero_sorteado = numero_sorteado
            self._cpf_sorteado = cpf
            return f'\nSORTEIO!\n\nNumero sorteado: {str(numero_sorteado).zfill(2)}\nCPF do ganhador: {cpf}\n'
        else:
            return f'\nSORTEIO!\n\nNumero sorteado: {str(self._numero_sorteado).zfill(2)}\nCPF do ganhador: {self._cpf_sorteado}\n'

    def realizar_sorteio(self):
        numero_sorteado = random.randint(0, self._tabela_rifa.get_tamanho())
        cpf = self._tabela_rifa.get(numero_sorteado - 1)
        return cpf, numero_sorteado

    def imprimir_cpf(self, valor):
        v = []
        for i, item in enumerate(self._tabela_rifa.get_tabela()):
            if len(item) != 0:
                for entry in item:
                    if entry.valor == valor:
                        v.append(f'{str(entry.chave).zfill(2)}')
        return f'CPF: {valor}\nNumeros comprados: {v}'
    
    def esgotou(self):
        return len(self._comprados) == self._tabela_rifa.get_tamanho()

    def get_tamanho(self):
        return self._tabela_rifa.get_tamanho()

