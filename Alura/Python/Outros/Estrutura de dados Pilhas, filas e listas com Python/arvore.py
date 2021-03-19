from ListaDupla.ListaEncadeadaDupla import *

class ListaDeNodos(ListaEncadeadaDupla):


    def __init__(self):
        super().__init__()

    def imprimir(self, nivel):
        atual = self.inicio
        for i in range(self.quantidade):
            atual.valor.imprimir(nivel)
            atual = atual.proximo
    
    def imprimirLarg(self, nivel):
        atual = self.inicio
        for i in range(self.quantidade):
            atual.valor.imprimirLargura(nivel)
            atual = atual.proximo

    def localizar_nodo(self, conteudo):
        atual = self.inicio
        for i in range(self.quantidade):
            encontrado = atual.valor.localizar_nodo(conteudo)
            if encontrado:
                return encontrado
            atual = atual.proximo
    
    def posicao(self, conteudo):
        atual = self.inicio
        for i in range(self.quantidade):
            if atual.valor.conteudo == conteudo:
                return i 
            else:
                atual = atual.valor

class Nodo():

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None
        
    
    def __repr__(self):
        return self.conteudo

    def imprimir(self, nivel=0):
        print(f'{"    "*nivel} - {self.conteudo}')
        # print(f'{nivel} - {self.conteudo}')
        if self.filhos:
            self.filhos.imprimir(nivel+1)

    def imprimirLargura(self, nivel=0):
        global largura
        try:
            largura[nivel].append(self.conteudo)
        except IndexError:
            largura.append([])
            largura[nivel].append(self.conteudo)
        if self.filhos:
            self.filhos.imprimirLarg(nivel+1)
        return largura

    def inserir_filho(self, filho):
        if self.filhos is None:
            self.filhos = ListaDeNodos()
        nodo = Nodo(filho)
        nodo.pai = self
        self.filhos.inserir_fim(nodo)

    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)

    def remover(self):
        if self.pai:
            posicao = self.pai.filhos.posicao(self.conteudo)
            return self.pai.filhos.remover(posicao)
        else:
            return self



class Arvore():


    def __init__(self, conteudo):
        self.raiz = Nodo(conteudo)
    
    def imprimir(self):
        self.raiz.imprimir()
    
    def imprimirLargura(self):
        self.raiz.imprimirLargura()
        return largura

    def localizar_nodo(self, conteudo):
        return self.raiz.localizar_nodo(conteudo)

    def inserir_nodo(self, pai, filho):
        nodo_pai = self.localizar_nodo(pai)
        if nodo_pai:
            nodo_pai.inserir_filho(filho)

    def remover_nodo(self, conteudo):
        encontrado = self.raiz.localizar_nodo(conteudo)
        if encontrado:
            if encontrado is self.raiz:
                self.raiz = None
            else:
                encontrado.remover()
        else:
            return encontrado
