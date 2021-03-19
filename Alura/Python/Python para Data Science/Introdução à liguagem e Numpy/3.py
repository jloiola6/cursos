import numpy as np 

# A lista não suporta a operação entre 1 inteiro e uma lista, ao contrário do array numpy
km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]
# idade = 2019 - anos     # DA ERRO!

# No Array numpy é suportado a operação entre um inteiro e o arry todo
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
idade = 2019 - anos
print(idade)



# Operações entre Arrays simples
km_media = km / idade
print(km_media) #Percebe-se que quando ele dividiu o valor de 0, que esta no array de idade, ele devolveu um valor nulo. No numpy é descrito como nam(Not a Number)

# O resultado é o mesmo, percebe-se que a operação que ele faz é a mesma
print(44410. / (2019-2003)) 
print(5712. / (2019-1991)) 



#Operações com Arrays de 2 dimensões
dados = np.array([km, anos]) # Estamos passando por parametros os arrays criados a cima para criar um Array de 2 dimensões.
print(dados)
print(dados.shape) # Retorna uma tupla com as informações de linhas e colunas 

km_media = dados[0] / (2019 - dados[1])
print(km_media)



# Fatiamento com Arrays numpy
contador = np.arange(10)
print(contador)
print(contador[1:4]) # Ele pega do indice 1 até o indice 4 (Quando ele chega no 4 ele para operação)
print(contador[1:8:2]) #Ele pega do indice 1 até o indice 8 mas vai dar um passo de 2
print(contador[::2]) #Ele pegar do começo até o fim e dando um passo de 2, resultando em mostrar os numeros pares
print(contador[1::2]) #Ele pegar do começo até o fim e dando um passo de 2, resultando em mostrar os numeros impares

#Realizar o calculo médio de tres elementos da array
km_media = dados[0][1:4] / (2019 - dados[1][1:4])
# km_media = dados[0, 1:4] / (2019 - dados[1, 1:4])  #Forma diferente!!!!

print(km_media)

#Indexação com Booleanos
print(contador > 5) # Aqui ele vai retornar, de forma booleana, os valores da array que são maiores que 5
print(contador[contador > 5]) # Aqui ele vai retornar os valores da array que são maiores que 5

print(dados[1] > 2000) # Aqui ele vai retornar, de forma booleana, os valores da array que são maiores que 2000
dados = dados[:, dados[1] > 2000] # É utilizado o ":" pois eles iremos usar todos os elementos da array, no caso as 2 linhas
print(dados)
km_media = dados[0] / (2019 - dados[1])
print(km_media)

