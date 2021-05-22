function criarProduto(nome, preco) {
    return {
        /* Se o nome da chave for o mesmo da variavel nao precisa do ":"
        nome,
        preco*/
        nome: nome,
        preco: preco,
        desconto: 0.1
    }
}

console.log(criarProduto("Notebook", 2199.49))
console.log(criarProduto("iPad", 1199.49))