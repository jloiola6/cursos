#Built-in function
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)

#Acessando os valores do dicionario
valores = []
for i in dados.values():
    valores.append(i)
print(valores)

print(list(dados.values())) #Criamos uma lista sem precisa pecorrer o dicionario (FORMA EFICIENTE)

#somando os valores do Dicionário (FORMA ANTIGA)
soma = 0
for i in dados.values():
    soma += i
print(soma)

print(sum(dados.values())) #Realizamos uma soma sem precisar pecorrer o dicionario (FORMA EFICIENTE)
print(sum(dados.values(), 10000)) #Se colocarmos um valor após é pq vamos iniciar a soma com o valor passado por parametro

help() #Use o help para conseguir ajuda sobre as funções padrões do python