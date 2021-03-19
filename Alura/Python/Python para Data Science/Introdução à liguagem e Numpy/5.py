import numpy as np 

ano = np.loadtxt('carros-anos.txt', dtype = int)
km = np.loadtxt('carros-km.txt')
valor = np.loadtxt('carros-valor.txt')
print(km.shape)
print(ano.shape)
print(valor.shape)

dataset = np.column_stack((ano, km, valor)) #Cria uma array com as informações elaboradas por colunas, ou seja, a pirmeira coluna irá ter os dados de ano, a segunda os dados de km e a terceira os dados de valor
print(dataset.shape)
# print(dataset) # Comentado pois fica muito grande kkkkk

print(np.mean(dataset, axis=0)) # Retorna a média dos elementos do array ao longo do eixo especificado. Lembrando que axis=0 ele faz o calculo pelas colunas e axis=1 ele faz o calculo pelas linhas.
print(np.mean(dataset[:,1], axis=0)) # Retorna a média dos elementos da segunda coluna, que no caso são os quilometros

print(np.std(dataset[:, 2])) # Retorna o desvio padrão dos elementos do array ao longo do eixo especificado
print(dataset.sum(axis=0)) # Somar todas os elementos de cada coluna
print(np.sum(dataset, axis=0)) # (FORMA DIFERENTE) Somar todos os elementos de cada coluna



