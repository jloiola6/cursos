from Lista_Encadeada import *

class Loja():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f"{self.nome}\n  {self.endereco}"

def main():
    loja1 = Loja('Mercadinho', 'Rua da Laranjeiras, 12')
    loja2 = Loja('Hortifruti', 'Rua do Pomar, 300')
    loja3 = Loja('Padaria', 'Rua das Flores, 600')
    loja4 = Loja('Supermercado', 'Alameda Santos, 400')
    loja5 = Loja('Mini Mercado', 'Rua da Fazenda, 900')
    loja6 = Loja('Quitanda', 'Avenida Rio Branco, 34')

    lista = ListaEncadeada()
    lista.inserir_inicio(loja1)
    lista.inserir_inicio(loja2)
    lista.inserir_inicio(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover_inicio()
    print(f'\nRemovido o valor: {removido}')

    removido = lista.remover_inicio()
    print(f'\nRemovido o valor: {removido}')

    removido = lista.remover(2)
    print(f'\nRemovido o valor: {removido}')

    removido = lista.remover(lista.quantidade - 1)
    print(f'\nRemovido o valor: {removido}')


    print(lista.item(10))


    lista.inserir_inicio(loja3)
    print(lista.quantidade)
    lista.imprimir()

main()