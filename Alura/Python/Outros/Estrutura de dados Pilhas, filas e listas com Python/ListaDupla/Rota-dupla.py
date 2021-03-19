from ListaEncadeadaDupla import *

class Loja():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'* {self.nome} - {self.endereco}'

def situacao(lista):
    print(f'Quantidade {lista.quantidade}')
    lista.imprimir()

def main():
    loja1 = Loja('Minimercado', 'Rua das FLores, 12')
    loja2 = Loja('Hortifruti', 'Avenida das Borboletas, 23')
    loja3 = Loja('Padaria Pão Quente', 'Praça da Ávore')
    loja4 = Loja('Supermercado', 'Rua do Pomar, 23')
    loja5 = Loja('Mercado', 'Rua das Fores, 98')
    loja6 = Loja('Quitanda', 'Rua da Fazenda, 899')
    loja7 = Loja('Minimercado das Frutas', 'Avenida do Bosque, 66')
    loja8 = Loja('Supermercado das Frutas', 'Rua do Pomar, 600')
    loja9 = Loja('Hortifruti da Terra', 'Rua das Laranjeiras, 800')
    loja10 = Loja('Mercado do Campo', 'Rua da Fazenda, 1500')

    lista = ListaEncadeadaDupla()

    lista.inserir_inicio(loja1)
    lista.inserir_inicio(loja2)
    lista.inserir_inicio(loja3)

    lista.inserir_fim(loja4)
    lista.inserir_fim(loja5)
    lista.inserir_fim(loja6)

    lista.inserir(2, loja7)
    lista.inserir(7, loja8)
    lista.inserir(0, loja9)
    lista.inserir(6, loja10)

    situacao(lista)

    removido = lista.remover_inicio()
    print(f'\nRemovido do inicio: {removido}')
    situacao(lista)

    removido = lista.remover_fim()
    print(f'\nRemovido do fim: {removido}')
    situacao(lista)

    removido = lista.remover(1)
    print(f'\n\Removido da posição 1: {removido}')
    situacao(lista)

    removido = lista.remover(5)
    print(f'\n\nRemovido da posição 5: {removido}')
    situacao(lista)

    removido = lista.remover(0)
    print(f'\n\nRemovido da posição 0: {removido}')
    situacao(lista)

    removido = lista.remover(4)
    print(f'\n\nRemovido da posição 4: {removido}')
    situacao(lista)


main()