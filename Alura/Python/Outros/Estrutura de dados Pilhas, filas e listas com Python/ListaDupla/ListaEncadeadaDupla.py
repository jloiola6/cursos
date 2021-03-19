class NoDupla():

    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
        

class ListaEncadeadaDupla():


    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim
    
    @property
    def quantidade(self):
        return self._quantidade

    def _inserir_vazia(self, valor):
        celula = NoDupla(valor)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.valor

    def _validar_posicao(self, posicao):
        if 0<= posicao < self.quantidade:
            return True
        raise IndexError(f'Posição inválida: {posicao}')

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        metade = self.quantidade // 2
        if posicao < metade:
            atual = self.inicio
            for i in range(posicao):
                atual = atual.proximo
            return atual
        else:
            atual = self.fim
            for i in range(posicao+1, self.quantidade)[::-1]:
                atual = atual.anterior
            return atual

    def inserir_inicio(self, valor):
        if self.quantidade == 0:
            return self._inserir_vazia(valor)
        else:
            celula = NoDupla(valor)
            celula.proximo = self.inicio
            self._inicio.anterior = celula
            self._inicio = celula
            self._quantidade += 1

    def imprimir(self):
        atual = self.inicio
        for i in range(self.quantidade):
            print(atual.valor)
            atual = atual.proximo

    def inserir_fim(self, valor):
        if self.quantidade == 0:
            return self._inserir_vazia(valor)
        else:
            celula = NoDupla(valor)
            celula.anterior = self.fim
            self.fim.proximo = celula
            self._fim = celula
            self._quantidade += 1

    def inserir(self, posicao, valor):
        if posicao == 0:
            return self.inserir_inicio(valor)
        elif posicao == self.quantidade:
            return self.inserir_fim(valor)
        else:
            esquerda = self._celula(posicao-1)
            direita = esquerda.proximo
            celula = NoDupla(valor)
            celula.proximo = direita
            celula.anterior = esquerda
            esquerda.proximo = celula
            direita.anterior = celula
            self._quantidade += 1
        
    def _remover_ultimo(self):
        if self.quantidade == 1:
            removido = self.inicio
            self._inicio = None
            self._fim = None
            self.quantidade -= 1
            return removido.valor

    def remover_inicio(self):
        if self.quantidade == 1:
            return self._remover_ultimo()
        else:
            removido = self.inicio
            self._inicio = removido.proximo
            self._inicio.anterior = None
            removido.proximo = None
            self._quantidade -= 1
            return removido.valor

    def remover_fim(self):
        if self.quantidade == 1:
            return self._remover_ultimo()
        else:
            removido = self.fim
            self._fim = removido.anterior
            self.fim.proximo = None
            removido.anterior = None
            self._quantidade -= 1
            return removido.valor

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_inicio()
        elif posicao == self._quantidade -1:
            return self.remover_fim()
        else:
            removido = self._celula(posicao)
            esquerda = removido.anterior
            direita = removido.proximo
            removido.proximo = None
            removido.anterior = None
            esquerda.proximo = direita
            direita.anterior = esquerda
            self._quantidade -= 1
            return removido.valor

    

