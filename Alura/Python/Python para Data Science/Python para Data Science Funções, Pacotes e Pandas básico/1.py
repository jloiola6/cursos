import pandas as pd # Pandas só esta funcionando na versão 3.6 do python
# pd.set_option('display.max_rows', 100) # Declaramso o numero maximo de linha que sera mostrado
# pd.set_option('display.max_columns', 10) # Declaramso o numero maximo de colunas que serão mostrado

dataset = pd.read_csv('Python_Data_Science\Pandas\data\db.csv', sep= ';') # Fazendo a leitura de um arquivo .csv e declarando um separador 
print(dataset)
print(dataset.dtypes) # Descobrir os tipos de dados associado em cada coluna

print(dataset[['Quilometragem', 'Valor']].describe()) # Aqui obtemos um conjunto de destatísticas descritivas dessas variáveis que foram passadas
print(dataset.info) # Adquirie informações sobre a colunas de dados aceitos