from ListaDupla.ListaEncadeadaDupla import *

class Fila():

    def __init__(self):
        self.fila = ListaEncadeadaDupla()

    def entrar(self, valor):
        self.fila.inserir_fim(valor)

    def sair(self):
        return self.fila.remover_inicio()

    @property
    def vazia(self):
        return self.fila.quantidade == 0

    @property
    def mostrar_pedidos(self):
        self.fila.imprimir()

