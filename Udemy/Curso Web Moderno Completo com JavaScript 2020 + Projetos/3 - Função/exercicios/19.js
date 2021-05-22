function pedido(codigo, qtd) {
    switch (codigo) {
    case 100:
        console.log(`R$${qtd*3.00}`)
        break
    case 200:
        console.log(`R$${qtd*4}`)
        break
    case 300:
        console.log(`R$${qtd*5.50}`)
        break
    case 400:
        console.log(`R$${qtd*7.50}`)
        break
    case 500:
        console.log(`R$${qtd*3.50}`)
        break
    case 600:
        console.log(`R$${qtd*2.80}`)
        break
    default:
        console.log("Código inválido")
    }
}

pedido(100, 2)