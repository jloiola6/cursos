function getPreco(imposto = 0, moeda = "R$") {
    return `${moeda} ${this.preco * (1 - this.desc) * (1 + imposto)}`
}

const produto = {
    nome: 'Notebook',
    preco: 4589,
    desc: 0.15,
    getPreco
}

console.log(getPreco()) // NAN

global.preco = 20
global.desc = 0.1
console.log(getPreco()) // Pegando precos globais
console.log(produto.getPreco()) // Pegando preco do objeto produto


const carro = { preco: 49990, desc: 0.20 }

console.log(getPreco.call(carro))
console.log(getPreco.apply(carro))

// Diferenças de usos do parametros do call e apply
console.log(getPreco.call(carro, 0.17, "$"))
console.log(getPreco.apply(global, [0.17, "$"]))
