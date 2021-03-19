// Função sem retorno 
function imprimirSoma(a, b){
    console.log(a + b)
}

imprimirSoma(2, 3)
imprimirSoma(2) // como não foi passado o valor b, a função irá tentar somar um valor com undefined e retornara NAN
imprimirSoma() // como não foi passado o valor a e b, a função irá tentar somar um valor com undefined e retornara NAN

// Função com retorno
function soma(a, b = 0) { // definindo um valor padrão caso não seja passado por parametro
    return a + b
}

console.log(soma(2, 3))
console.log(soma(2))
console.log(soma()) // como não foi passado o valor a, a função irá tentar somar um valor com undefined e retornara NAN