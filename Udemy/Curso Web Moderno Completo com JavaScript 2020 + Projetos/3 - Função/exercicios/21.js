function planoSaude (idade) {
    let pagamento 
    if (idade < 10) {
        pagamento = 80
    } else if (10 < idade < 30 ) {
        pagamento = 50
    } else if (30 < idade < 60 ) {
        pagamento = 95
    } else {
        pagamento = 130
    }

    return pagamento
}

console.log(planoSaude(35))