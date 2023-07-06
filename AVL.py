from no import No
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
    
    def add(self, info1, registro, chave):            
        if self.__raiz == None:
            self.__raiz = No(info1, registro, chave)
            self.__raiz.addNumeros(chave)
            return self.__raiz
        else:
            no = self.busca(registro)
            if no == None:
                no = self.__add(info1, registro, chave)
            else:
                no = self.__addNovo(registro, chave)

    def __add(self, raiz, info1, registro, chave):
        if not raiz:
            no = No(info1, registro, chave)
            no.addNumeros(chave)
            return no
        if registro < raiz.getRegistro(): 
            no = raiz.esq = self.__add(raiz.esq, info1, registro, chave)
            return no
        else: 
            no = raiz.dir = self.__add(raiz.dir, info1, registro, chave)
        raiz.altura = 1 + max(self.getAltura(raiz.esq), self.getAltura(raiz.dir))
        balance = self.getBalance(raiz) 
        if balance > 1 and registro < raiz.esq.registro: 
            return self.__dirRotate(raiz)
        if balance < -1 and registro > raiz.dir.registro: 
            return self.__esqRotate(raiz) 
        if balance > 1 and registro > raiz.esq.registro: 
            raiz.esq = self.__esqRotate(raiz.esq) 
            return self.__dirRotate(raiz)
        if balance < -1 and registro < raiz.dir.registro: 
            raiz.dir = self.__dirRotate(raiz.dir) 
            return self.__esqRotate(raiz)
        return no

    def __addNovo(self, registro, chave):
        no = self.busca(registro)
        no.addNumeros(chave)
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
    
    def busca(self, registro):
        if self.__raiz != None:
            dado = self.__busca(registro, self.__raiz)
            return None if dado is None else dado
        else:
            return None
    
    def __busca(self, registro, no):
        if registro == no.getRegistro():
            return no
        elif registro < no.getRegistro() and no.esq != None:
            return self.__busca(registro, no.esq)
        elif registro > no.getRegistro() and no.dir != None:
            return self.__busca(registro, no.dir)
        else:
            return None
        