from AVL import AVL
from comprador import Comprador
from hashtable import TabelaHash

compradores = AVL()
numeros = TabelaHash(5)

def comprar(nome, cpf, numero):
    no = compradores.busca(cpf)
    if no == None:
        no = compradores.addNovoComprador(nome, cpf, numero)
        numeros.addObjeto(no, numero)
    else:
        no = compradores.addNovoNumero(cpf, numero)
        numeros.addObjeto(no, numero)

def buscar(cpf):
    return compradores.busca(cpf)

comprar('Raiza', '06824224448', 3)
comprar('Lavinia', '12345678912', 2)
comprar('Lavinia', '12345678912', 5)
print(buscar('12345678912'))
print('')
print(numeros)