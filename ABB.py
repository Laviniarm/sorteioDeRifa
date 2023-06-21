from Pessoa import Pessoa

class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)

class ABB:        
    def __init__(self):
        self.__raiz = None

    def estaVazia(self)->bool:
        return self.__raiz == None
    
    def getRaiz(self)->any:
        return self.__raiz.carga if self.__raiz is not None else None

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is not None:
            self.__emordem(no.esq)
            print(f'{no.carga}',end=' ')
            self.__emordem(no.dir)
    
    def desordem(self):
        return self.__desordem(self.__raiz)
    
    def __desordem(self, no):
        if no is not None:
            self.__desordem(no.dir)
            print(f'{no.carga}',end=' ')
            self.__desordem(no.esq)
    
    def esvaziar(self):
        cursor = self.__raiz
        if cursor != None:
            if cursor.esq != None:
                cursor.esq = None
            elif cursor.dir != None:
                cursor.dir = None
            self.__raiz = None
        else:
            return

    def add(self, carga:any)->bool:
        if(self.__raiz == None):
            self.__raiz = No(carga)
        else:
            self.__add(carga, self.__raiz)   

    def __add(self, carga, no):
        if (carga.getCPF() < no.carga.getCPF()):
            if(no.esq != None):
                self.__add(carga, no.esq)
            else:
                no.esq = No(carga)
        else:
            if(no.dir != None):
                self.__add(carga, no.dir)
            else:
                no.dir = No(carga)

    def __count(self, no:'No')->int:
        if no is None:
            return 0
        else:
            return 1 + self.__count(no.esq) + self.__count(no.dir)

    def __len__(self):
        return self.__count(self.__raiz)

    def busca(self, chave:any)->any:
        if(self.__raiz != None):
            no = self.__busca(chave, self.__raiz)
            return no.carga.getCPF() if no is not None else None
        else:
            return None
    
    def __busca(self, chave:any, no:No):
        if (chave == no.carga.getCPF()):
            return no
        elif (chave < no.carga.getCPF() and no.esq != None):
            return self.__busca(chave, no.esq)
        elif (chave > no.carga.getCPF() and no.dir != None):
            return self.__busca(chave, no.dir)
        else:
            return None
    
    def __str__(self):
        if self.__raiz is None:
            return "Árvore vazia"
        else:
            return self._str_recursive(self.__raiz)

    def _str_recursive(self, no):
        s = ""
        if no is not None:
            s += self._str_recursive(no.esq)
            s += str(no.carga) + "\n"
            s += self._str_recursive(no.dir)
        return s

if __name__ == "__main__":
    c = Cliente('06824224448')
    c.addNumero(10)
    c.addNumero(15)
    c.addNumero(8)

    c2 = Cliente('11032391472')
    c2.addNumero(5)
    c2.addNumero(45)
    c2.addNumero(37)

    a = ABB()
    a.add(c)
    a.add(c2)
    # print(a)
    a.esvaziar()
    print(a)