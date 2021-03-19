// Armazenando uma função em uma variável
const imprimirsoma = function (a, b){
    console.log(a + b)
}

imprimirsoma(2, 3)

// Armazenando uma função arrow em uma variável
const soma = (a, b) => {
    return a + b
}

console.log(soma(2, 3))

// Retorno implicito  (SOMENTE UMA LINHA)
const subtracao = (a, b) => a - b
console.log(subtracao(2, 3))

const imprimir2 = a => console.log(a)
imprimir2('Teste de Função')