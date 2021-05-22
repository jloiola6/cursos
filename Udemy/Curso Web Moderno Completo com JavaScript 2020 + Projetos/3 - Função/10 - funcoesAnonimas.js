const soma = function (x, y) { // funcões anonimas são funções que não contém nome
    return x + y
}

const imprimirResultado = function (a, b, operacao = soma) {
    console.log(operacao(a, b))
}
imprimirResultado(3, 4)
imprimirResultado(3, 4, soma)
imprimirResultado(3, 4, function (x, y) {
    return x - y
})
imprimirResultado(3, 4, (x, y) => x * y)

const pessoa = {
    falar: function () {
        console.log('Opa!')
    }
    // falar() {  Outra forma de criar uma funcao na chave 
    //     console.log('Opa!')
    // }
}

pessoa.falar()