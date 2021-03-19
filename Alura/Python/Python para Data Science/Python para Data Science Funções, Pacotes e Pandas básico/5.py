import pandas as pd

separador = '\n'*2 + '-'*40 + '\n'

#Series:
#   - São arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de index.

# exem_series = pd.Series(dados, index = index)

carros = ['Jetta Variant', 'Passat', 'Crossfox']

exem_series = pd.Series(carros)
print(separador, '*1: \n', exem_series)


#DataFrame:
#   - Estrutura de dados tabular bidimensional com rótulos nas linhas e coluas

#exem_dataframe = pd.DataFrame(dados, index= index, colums= colums)

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

exem_dataframe = pd.DataFrame(dados)
print(separador, '*2: \n', exem_dataframe)

#Alterar as colunas 
exem_dataframe = exem_dataframe[['Nome', 'Ano', 'Motor', 'Quilometragem', 'Zero_km', 'Valor']]
print(separador, '*3: \n', exem_dataframe)

#Criando DataFrames a partir de um dicionario
dados = {
    'Nome': ['Jetta Variant','Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel'], 
    'Ano': [2003, 1991, 1990], 
    'Quilometragem': [44410.0, 5712.0, 37123.0], 
    'Zero_km': [False, False, False], 
    'Valor': [88078.64, 106161.94, 72832.16]}

exem_dataframe = pd.DataFrame(dados)
print(separador, '*4: \n', exem_dataframe)

#Criando DataFrames a partir de um arquivo
exem_dataframe =  pd.read_csv('Python_Data_Science\Pandas\data\db.csv', sep = ';')
print(separador, '*5: \n', exem_dataframe)
 
#Colocando uma coluna como indice no DataFrame (0 == Nome, 1 == Motor e assim por diante)
exem_dataframe =  pd.read_csv('Python_Data_Science\Pandas\data\db.csv', sep = ';', index_col= 0)
print(separador, '*6: \n', exem_dataframe)



#Seleções com DataFrames (É retornado uma Series)
print(separador, '*7: \n', exem_dataframe['Valor'])

#Selecionando mais de uma coluna (É retornado um DataFrame)
print(separador, '*8: \n', exem_dataframe[['Valor', 'Motor']])

#Seleção de Linhas
print(separador, '*9: \n', exem_dataframe[0:3])


#Seleção com .loc
#   - Retorna uma Series com as informações da linha do Passat
print(separador, '*10: \n', exem_dataframe.loc['Passat'])
#   - Retorna um DataFrame com as informações dos indices passadas por parametro
print(separador, '*11: \n', exem_dataframe.loc[['Passat', 'DS5']])
#   - Retorna um DataFrame com as colunas dos indices passadas por parametro 
print(separador, '*12: \n', exem_dataframe.loc[['Passat', 'DS5'], ['Motor', 'Valor']])


#Seleção com .iloc 
#   - Seleciona com base nos indices
print(separador, '*13: \n', exem_dataframe.iloc[1]) #Series

print(separador, '*14: \n', exem_dataframe.iloc[[1]]) #DataFrame

print(separador, '*15: \n', exem_dataframe.iloc[1:4]) # Retorna mais de uma linha

print(separador, '*16: \n', exem_dataframe.iloc[[0, 5, 2]]) # Retorna na ordem de colunas que eu especifiquei

print(separador, '*17: \n', exem_dataframe.iloc[[1, 42, 22], [0, 5, 2]]) # Retorna na ordem de colunas e as linhas que eu especifiquei

print(separador, '*18: \n', exem_dataframe.iloc[:3, [0, 5, 2]]) # Retorna na ordem de colunas e as linhas que eu especifiquei


#Realizando Querries/Consultas com DataFrame
print(separador, '*19: \n', exem_dataframe.Motor) # Retorna os dados de acordo com a coluna desejada

print(separador, '*20: \n', exem_dataframe.Motor == 'Motor Diesel') #Retorna uma Series de dados de acordo com a coluna desejada em forma Bool

print(separador, '*21: \n', exem_dataframe[exem_dataframe.Motor == 'Motor Diesel']) #Retorna os dados de acordo com a condição 

print(separador, '*22: \n', exem_dataframe[(exem_dataframe.Motor == 'Motor Diesel') & (exem_dataframe.Zero_km == True)]) #Retorna os dados de acordo com as condições (and = &, or = /)

#Utilizando o método Query
print(separador, '*23: \n', exem_dataframe.query('Motor == "Motor Diesel" and Zero_km == True')) #Retorna os dados de acordo com as condições


#Interações com DataFrames
print(separador, '*24: \n', list(exem_dataframe.iterrows())) #Criou uma lista com tuplas pecorrendo todos os indices

#Operação para calcular a velocidade média
for indice, linha in exem_dataframe.iterrows():
    if (2019 - linha['Ano']) != 0: #Verificando que o valor seja diferente de zero
        exem_dataframe.loc[indice, 'km_media'] = linha['Quilometragem'] / (2019 - linha['Ano'])
    else:
        exem_dataframe.loc[indice, 'km_media'] = 0
print(separador, '*25: \n', exem_dataframe)


#Tratamento de Dados
print(separador, '*26: \n', exem_dataframe.info()) # Verificar informações do DataFrame de forma rápida

print(separador, '*27: \n', exem_dataframe.Quilometragem.isna()) # Retorna todo os valores, em bool, que são nulos ou não (True == Null, False == Not Null)

print(separador, '*28: \n', exem_dataframe[exem_dataframe.Quilometragem.isna()]) # Retorna somente os valores, em bool, que são nulos

exem_dataframe.fillna(0, inplace = True) #Aqui estamos alterando todos os valores que são nulos pelo valor passado por parametro.(É passado o inplace = True para salvar a alteração)

print(separador, '*29: \n', exem_dataframe.query('Zero_km == True')) #Conferindo que todos os dados foram alterados, de acordo com a operação acima

# Apagando os registro com algum valor nulo
exem_dataframe =  pd.read_csv('Python_Data_Science\Pandas\data\db.csv', sep = ';') # importanto o arquio novamente

exem_dataframe.dropna(subset= ['Quilometragem'], inplace = True) #Aqui estamos apagando todos os valores que são nulos pela coluna passada por parametro.(É passado o inplace = True para salvar a alteração)

print(separador, '*30: \n', exem_dataframe.query) #Conferindo que todos os dados foram alterados, de acordo com a operação acima

