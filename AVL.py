from comprador import Comprador
from hashtable import TabelaHash

class AVL:
    def __init__(self):
        self.__raiz = None

    def estaVazia(self):
        return self.__raiz == None
    
    def getAltura(self, no):
        if no is None:
            return 0
        else:
            return no.altura
        
    def getBalance(self, no):
        if not no: 
            return 0  
        return self.getAltura(no.esq) - self.getAltura(no.dir)
    
    def addNovoComprador(self, nome, cpf, numero):            
        if self.__raiz == None:
            self.__raiz = Comprador(nome, cpf, numero)
            self.__raiz.addNumeros(numero)
            return self.__raiz

        else:
            return self.__addNovoComprador(self.__raiz, nome, cpf, numero)
    
    def __addNovoComprador(self, raiz, nome, cpf, numero):
        if not raiz:
            no = Comprador(nome, cpf, numero)
            no.addNumeros(numero)
            return no
        if cpf < raiz.getCPF(): 
            no = raiz.esq = self.__addNovoComprador(raiz.esq, nome, cpf, numero)
            return no
        else: 
            no = raiz.dir = self.__addNovoComprador(raiz.dir, nome, cpf, numero)
        raiz.altura = 1 + max(self.getAltura(raiz.esq), self.getAltura(raiz.dir))
        balance = self.getBalance(raiz) 
        if balance > 1 and cpf < raiz.esq.cpf: 
            return self.__dirRotate(raiz)
        if balance < -1 and cpf > raiz.dir.cpf: 
            return self.__esqRotate(raiz) 
        if balance > 1 and cpf > raiz.esq.cpf: 
            raiz.esq = self.__esqRotate(raiz.esq) 
            return self.__dirRotate(raiz)
        if balance < -1 and cpf < raiz.dir.cpf: 
            raiz.dir = self.__dirRotate(raiz.dir) 
            return self.__esqRotate(raiz)
        return no
    
    def addNovoNumero(self, cpf, numero):
        return self.__addNovoNumero(cpf, numero)

    def addNovoNumero(self, cpf, numero):
        no = self.busca(cpf)
        no.addNumeros(numero)
        return no
    
    def __esqRotate(self, no):
        novaRaiz = no.dir
        T2 = novaRaiz.esq 
        novaRaiz.esq = no
        no.dir= T2
        no.altura = 1 + max(self.getAltura(no.esq), self.getAltura(no.dir)) 
        novaRaiz.altura = 1 + max(self.getAltura(novaRaiz.esq), self.getAltura(novaRaiz.dir)) 
        return novaRaiz
    
    def __dirRotate(self, no):
        novaRaiz = no.esq 
        T2 = novaRaiz.dir 
        novaRaiz.dir = no 
        no.esq = T2 
        no.altura = 1 + max(self.getAltura(no.esq), self.getAltura(no.dir)) 
        novaRaiz.altura = 1 + max(self.getAltura(novaRaiz.esq), self.getAltura(novaRaiz.dir)) 
        return novaRaiz
    
    def busca(self, cpf):
        if self.__raiz != None:
            dado = self.__busca(cpf, self.__raiz)
            return None if dado is None else dado
        else:
            return None
    
    def __busca(self, cpf, no):
        if cpf == no.getCPF():
            return no
        elif cpf < no.getCPF() and no.esq != None:
            return self.__busca(cpf, no.esq)
        elif cpf > no.getCPF() and no.dir != None:
            return self.__busca(cpf, no.dir)
        else:
            return None
        