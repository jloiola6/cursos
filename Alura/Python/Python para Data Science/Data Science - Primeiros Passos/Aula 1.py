# %%
#ATENÇÃO DEVE SE COLOCAR "cell" no incio para abrir a página de vizualização dos gráficos
# SHIFT + ENTER é o atalho

import pandas as pd
import matplotlib.pyplot as plt #Para plotar e gerar gráficos
# import seaborn as sns 


separador = '\n'*2 + '-'*40 + '\n'

notas = pd.read_csv("aula0/ml-latest-small/ratings.csv") # Importando um csv
print(separador + '*1\n', notas.head) # Mostra somente os 5 primeiros elementos

print(separador + '*2\n', notas.shape) # Retorna o formato da tabela (linhas, colunas)

notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento'] #alterando os nomes das colunas da tabela
print(separador + '*3\n', notas.head) # Retorna o formato da tabela (linhas, colunas)

print(separador + '*4\n', notas['nota']) # Vizualizando todos os elementos de uma coluna
print(separador + '*5\n', notas['nota']) # Vizualizando todos os elementos de uma coluna

print(separador + '*6\n', notas['nota'].unique()) # Vizualizando os valores unicos

print(separador + '*7\n', notas['nota'].value_counts()) # Contar os valores(nesse caso, quantidades de pessoas que votaram) que cada nota recebeu

print(separador + '*7\n', notas['nota'].mean()) # Calcular a média

print(separador + '*8\n', notas['nota'].median()) # Calcular a mediana

print(separador + '*9\n', notas.nota.describe()) # Descrever a nossa Serie

# VISUALIZANDO DADOS COM HISTOGRAMA E BOXPLOT

# notas.nota.plot() #Plotamos os dados 

# notas.nota.plot(kind= 'hist') #Plotamos os dados como histograma

#UTILIZANDO O matplotlib
# ----------------------------------------------------
plt.plot(notas.nota) #Plotamos os dados 
plt.show() #Visualizamos o gráfico criado

plt.hist(notas.nota) # Criamos um histograma
plt.xlabel('Descrição x')
plt.ylabel('Descrção y')
plt.show() #Visualizamos o gráfico criado
# # ----------------------------------------------------

#USANDO O SEABORN
# sns.boxplot(notas.nota)
# %%
