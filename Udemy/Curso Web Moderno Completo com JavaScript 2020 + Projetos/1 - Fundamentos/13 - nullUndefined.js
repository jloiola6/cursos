let valor // Não iniciado
console.log(valor)

valor = null
console.log(valor) // Ausencia do valor

const produto = {}
console.log(produto.preco)
console.log(produto)

produto.preco = 3.50
console.log(produto.preco)

produto.preco = null
console.log(!!produto.preco)
console.log(produto)