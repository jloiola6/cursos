import numpy as np 
import time

#Criar uma array 
x1 = np.arange(10)

#Criar Aray no Numpy a partir de uma lista
km = np.array([1000, 2300, 4987, 1500])
# print(type(km)) #Vizualizar o tipo da variavel
# print(km.dtype) #Vizualizar o tipo de dado armazenado dentro da array

#Criar Array Numpy por dados externos
km = np.loadtxt('carros-km.txt', int)
# print(km) 

#Criar Arrays com 2 dimensões (Matrizes)
dados = ['joão', 'roberto', 'Gabi', 'Thaís', 
        ['Kleber', 'Santana', 'Arthur', 'Moises'],
        ['Maria', 'Clovis', 'Carlos', 'Thyago']]
nomes = np.array(dados)
# print(nomes)
# print(nomes.shape) #Mostrar informações da Array (Quantidadesde linhas e colunas)



#Arrays são melhores que listas para desempenhos matemáticos (COMPARAÇÃO)
np_array = np.arange(1000000) #Criar um array com um milhão de elementos
py_list = list(range(1000000)) #Criar uma lista com um milhão de elementos

# Estamos dando um for nos dados e multiplicando por 2 100 vezes para testar.
inicio = float(time.time())
for _ in range(100): np_array *= 2 # Pode multiplicar os valores por 2 de uma vez só
fim = float(time.time())
print('Tempo do array: ', float(fim - inicio))

inicio = float(time.time())
for _ in range(100): py_list = [x * 2 for x in py_list] #Esta fazendo a mesma coisa que o array, porem o array Numpy não precisa de outro for, na lista o valor tem que ser multiplicado um por um
fim = float(time.time())
print('Tempo da lista: ', float(fim - inicio))



