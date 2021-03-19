import pandas as pd

separador = '\n'*2 + '-'*40 + '\n'

filmes = pd.read_csv('tmdb_5000_movies.csv')
print(separador + '*1\n', filmes.head) # Mostra somente os 5 primeiros elementos

print(separador + '*1\n', filmes.shape) 

print(separador + '*2\n', filmes.original_language.unique()) 



