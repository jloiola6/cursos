from Pilha.Lista_Encadeada import *

class Pilha():
     
    def __init__(self):
         self.pilha = ListaEncadeada()

    def empilhar(self, valor):
        self.pilha.inserir_inicio(valor)

    def desempilhar(self):
        return self.pilha.remover_inicio()
    
    @property
    def topo(self):
        return self.pilha.item(0)

    @property
    def vazio(self):
        return self.pilha.quantidade == 0