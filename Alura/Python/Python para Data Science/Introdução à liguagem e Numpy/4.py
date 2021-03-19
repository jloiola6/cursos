import numpy as np 

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

# -------------------Atributos numpy

print(dados.shape) # Retorna uma tupla com as informações de linhas e colunas 
print(dados.ndim) # Retona o numero de dimensões do array
print(dados.size) # Retorna o numero de elementos total que ele tem no array
print(dados.dtype) # Retorna o tipo de dados dos elementos dentro do array
print(dados.T) # Tranforma o que ta com linha em coluna. Ele é o equivalente a "dados.tranpose()""



# --------------------Métodos numpy
print(dados.tolist()) # Transforma uma array em uma lista do python

# Exemplo de aplicação do reshape
contador = np.arange(10) 
print(contador.reshape(5,2)) # Retorna um array que contem os mesmo dados com uma nova forma. Solicitei que ele crie um array com 5 linhas e 2 colunas

km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]
info_carros = km + anos # Junção de 2 listas
print(info_carros)

info_carros = np.array(info_carros).reshape(2,5, order='c') # Cria um array da lista e dar um reshape transformando em uma matriz com 2 linhas e 5 colunas
print(info_carros)

info_carros = np.array(info_carros).reshape(5, 2, order='f') # Cria um array da lista e dar um reshape transformando em uma matriz com 2 linhas e 5 colunas
print(info_carros)

'''
    No reshape existe a ordem que os elementos podem ser apresentados, por padrão pelo C. 
    No C ele vai usar a indexização da linguagem C
    No F ele vai usar a indexização da linguagem Fortran 
    Essa mudança pode ser util dependendo da forma que voce quer fazer o shape
'''

#Exemplo de aplicação resize
dados_new = dados.copy()
dados_new.resize(3, 5, refcheck = False) # É adicionado uma terceira linha com 5 colunas vazias (Lembre-se de colocar o refcheck para false)
print(dados_new)

dados_new[2] = dados_new[0] / (2019 - dados_new[1]) # Estamos dando o valor para os dados da 3 linha, colocando a km média, ou seja, na primeira linha temos o km, na segunda linha temos o ano e na terceira linha temos a quilometragem média
