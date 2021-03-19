# %%
import pandas as pd
import seaborn as sns

separador = '\n'*2 + '-'*40 + '\n'

filmes = pd.read_csv("aula0/ml-latest-small/movies.csv") # Importando um csv
filmes.columns = ['filmeId', 'titulo', 'genero'] #alterando os nomes das colunas da tabela

print(separador + '*1\n', filmes.head) # Mostra o cabeçalho do do DataFrame

notas = pd.read_csv("aula0/ml-latest-small/ratings.csv") # Importando um csv
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento'] #alterando os nomes das colunas da tabela

print(separador + '*2\n', notas.query('filmeId==1').nota.mean()) # Retornar só a média da coluna nota, cujo o filmeid for igual a 1.

print(separador + '*3\n', notas.query('filmeId==2').nota.mean()) # Retornar só a média da coluna nota, cujo o filmeid for igual a 2.

mediaPorFilme = notas.groupby('filmeId').mean().nota # Agrupamos todos os filmes e damos a média de cada um e extraimos somente a coluna Nota.
print(separador + '*4\n', mediaPorFilme.head) 

# mediaPorFilme.plot(kind='hist') # Gráfico pelo pandas

# sns.boxplot(mediaPorFilme) # Gráfico pelo Seaborn

print(separador + '*4\n', mediaPorFilme.describe()) 

sns.distplot(mediaPorFilme, bins= 10) #Gráfico em histograma do Seaborn. Bins são as caixinhas que irão ser apresentadas
# %%
