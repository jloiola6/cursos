import numpy as np

#Usa-se o loadtxt para carregar um arquivo txt
km = np.loadtxt('carros-km.txt')

ano = np.loadtxt('carros-anos.txt', dtype = int)

km_media = km / (2019-ano)

print(km_media)