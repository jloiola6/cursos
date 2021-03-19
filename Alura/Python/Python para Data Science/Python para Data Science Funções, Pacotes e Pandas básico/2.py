
##### TUPLAS #####
# Ao contrário da lista, Tuplas sõa imutáveis
nome = 'Passat'
valor = 153000
x = (nome, valor) #Criando um Tupla
print(x) 

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5']) # Criando uma tupla através de uma lista
print(nomes_carros)

print(nomes_carros[1]) # Acessando elementos de uma tupla (MESMA BASE DE LISTA)

for i in nomes_carros: # Pecorrer cada itens da tupla
    print(i)


# Desempacotamente de Tuplas

carro_1, carro_2, carro_3, carro_4 = nomes_carros # Cada variavel vai receber um valor referente ao elemento na tupla. Ex: carro_1 vai receber o valor de nomes_carros[0], por ser o primeiro elemento e assim sucessivamente

print(carro_1)
print(carro_2)
print(carro_3)
print(carro_4)

'''
    Utilizamos o "_" conhecido como sigle underscore para insinuar que a variavel tem q ser ignorada ou não "Não importa"

    Sometimes used as a name for temporary or insignificant variables (“don’t care”).
    Also: The result of the last expression in a Python REPL.
'''
_, A, _, B = nomes_carros # Aqui estamos ignorando o primeiro valor, criando uma variavel, ignorando o segundo e criando outra variavel

_, C, *_ = nomes_carros # Utilizamos o "*_" para ele ignorar todos os próximos
print(A)

# Zip()

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

resultado = list(zip(carros, valores)) # Ele cria varias tuplas linkando o valores com os carros de acordo com a posição
print(resultado)

for i in zip(carros, valores): # Pecorrendo cada tupla linkada
    print(i) # printa a tupla

for carro, valor in zip(carros, valores): # Pecorre a tupla linkada dando dois parametros dele
    print(carro, valor) # Printa cada elemento na tupla de acordo com os parametros acima

for carro, valor in zip(carros, valores): 
    if valor > 100000:
        print(carro)