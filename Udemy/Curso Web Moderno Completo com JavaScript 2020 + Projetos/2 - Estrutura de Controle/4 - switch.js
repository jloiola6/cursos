const imprimirResultado = function(nota) {
    switch (Math.floor(nota)) {
        case 10:
        case 9:
            console.log('Quadro de Honra')
            break // É obrigatório usar o "break" para ele não executar as operações a seguir, já todas vão ser verdades...
        case 8: case 7:
            console.log('Aprovado')
            break
        case 6: case 5: case 4:
            console.log('Reprovado')
            break
        case 3: case 2: case 1:
            console.log('Nota Inválida')
            break
        default:
            console.log('Nota Inválida')
    }       

    console.log('Fim')
}

imprimirResultado(10)
imprimirResultado(8.9)
imprimirResultado(6.55)
imprimirResultado(2.3)
imprimirResultado(-1)
imprimirResultado(11)