from arvore import *

largura = []

def main():
    livraria = Arvore('Livros') #Cria uma arvore com a raiz passada
    # livraria.imprimir()
    
    # Criando filhos para a raiz
    livraria.raiz.inserir_filho('Gastronomia')
    livraria.raiz.inserir_filho('Informática')
    livraria.raiz.inserir_filho('teste')

    #Criando filhos para as folhas criadas
    livraria.inserir_nodo('Gastronomia', 'Sobremesas')
    livraria.inserir_nodo('Sobremesas', 'Pudim')
    livraria.inserir_nodo('Sobremesas', 'Bolo')
    livraria.inserir_nodo('Sobremesas', 'Sorvete')

    livraria.inserir_nodo('Gastronomia', 'Almoço')
    livraria.inserir_nodo('Almoço', 'Bife Acebolado')
    livraria.inserir_nodo('Almoço', 'Churrasco')

    livraria.inserir_nodo('Informática', 'Linguagens')
    livraria.inserir_nodo('Linguagens', 'Python')
    livraria.inserir_nodo('Linguagens', 'Java')
    livraria.inserir_nodo('Linguagens', 'Go')

    livraria.imprimirLargura()

    
    # #Realizando Busca na arvore
    # encontrado = livraria.localizar_nodo('Churrasco')
    # print(f'\nEncontrado: {encontrado}')
    
    # encontrado = livraria.localizar_nodo('Python')
    # print(f'Encontrado: {encontrado}')
    
    # # Realizando uma busca que não apresenta resultado
    # encontrado = livraria.localizar_nodo('alif')
    # print(f'Encontrado: {encontrado}')

    # #Removendo uma folha da arvore
    # removido = livraria.remover_nodo('Gastronomia')
    # print(f'Removido: {removido}')

    livraria.imprimir()

main()