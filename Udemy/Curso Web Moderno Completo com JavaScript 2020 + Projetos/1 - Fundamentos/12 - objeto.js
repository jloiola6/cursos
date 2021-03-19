const prod1 = {} // Criei um objeto vazio
prod1.nome = 'Celular Ultra Mega' // É criado a chave/atributo dinamicamente
prod1.preco = 4998.90
prod1['Desconto Legal'] = 0.40 // Criando chaves/atributos com espaços... (EVITAR A O MÁXIMO)

console.log(prod1)

const prod2 = {
    nome: 'Camisa Polo',
    preco: 79.90,
    obj: {
        blabla: 1
    }
}

console.log(prod2)