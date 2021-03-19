# Dicionários

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

# Criando dicionários com Zip()
carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

dados = dict(zip(carros, valores))
print(dados) 

print(dados['Passat']) # Mostra o valor de acordo com a chave
print('João' in dados) # Verifica se existe determinada chave dentro do dicionario
print(len(dados)) # Mostra a quantidade de elementos no dicionario

dados['DS5'] = 124549.07 # Adcionando um valor ao dicionario
print(dados)

del dados['Passat'] # Deleta o valor de acordo com  a chave dele
print(dados)


# Realizar atualizações no dicionários

dados.update({'Passat': 106161.94}) # Caso não tenha nenhum valor com essa chave ele vai atualizar
print(dados)

dados.update({'Passat': 106161.95, 'Fusca': '150000'}) # Ele vai atualizar o valor de acordo com a chave e vai adcionar outro valor (pois a chave "Fusca" não existe)
dadosCopy = dados.copy() # Criar uma cópia dos dados
'''
    Atenção! 
    O método pop não funciona como lista quando utilizado em dicionários, ele não vai apagar o ultimo valor...
'''
print(dadosCopy.pop('Passat')) # Ele apagar o valor de acordo com a chave e retorna o mesmo
print(dadosCopy.pop('Passat', 'Chave não econtrada')) # Ele retorna a mensagem que definimos caso náo exista a chave passada

dadosCopy.clear() # Para remover todos os itens de um dicionário
print(dadosCopy)

print(dados.keys()) # Retorna uma lista com todas as chaves do dicionário
print(dados.values()) # Retorna uma lista com todas os valores do dicionário
for key in dados.keys():
    print(dados[key])

print(dados.items()) # É praticamente um Zip(   ) só que pra dicionários
for key, value in dados.items():
    print(key, value)
