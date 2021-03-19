const imprimirResultado = function(nota) {
    if (nota >= 7) {
        console.log('Aprovado!')
    } else {
        console.log('Reprovado!')
    }
}

imprimirResultado(10)
imprimirResultado(4)
imprimirResultado('Epa') // Por ser uma linguagem fracamente tipada ele permite passar e comparar um valor que não é do mesmo tipo