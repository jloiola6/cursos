from matplotlib import pyplot as plt

notas = [9, 5, 7, 2, 8, 1, 3, 9, 10, 2, 5, 4] # Eixo y
x = list(range(1, len(notas)+1)) #criamos uma lista q vai de 1 até a quantdade de elementos de notas. Isso é o eixo y 

plt.plot(x, notas, marker= '.') #criamos o gráfico e declaramos um marcador aonde os dados sõa absolutos.
plt.title('Notas de Matemática') # Declaramos um titulo
plt.xlabel('Provas') # Declaramos uma descrição de x
plt.ylabel('Notas') # Declaramos uma descrição de y 
plt.show() # Retorna o gráfico criado

