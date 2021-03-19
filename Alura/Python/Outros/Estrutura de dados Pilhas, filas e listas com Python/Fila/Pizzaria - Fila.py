from Fila import *

class Pedido():

    def __init__(self, pizza):
        self.pizza = pizza

    def __repr__(self):
        return self.pizza

def main():
    pizzaria = Fila()
    
    pedido1 = Pedido('Mussarela')
    pedido2 = Pedido('Calabresa')
    pedido3 = Pedido('Marguerita')
    pedido4 = Pedido('Rúcula')

    print(f'Recebendo pedido {pedido1}')
    pizzaria.entrar(pedido1)

    print(f'Recebendo pedido {pedido2}')
    pizzaria.entrar(pedido2)

    print(f'Recebendo pedido {pedido3}')
    pizzaria.entrar(pedido3)  
    
    pedido = pizzaria.sair()
    print(f'Fazendo pizza: {pedido}')
    print(f'A fila está vazia: {pizzaria.vazia}')

    pizzaria.mostrar_pedidos



main()