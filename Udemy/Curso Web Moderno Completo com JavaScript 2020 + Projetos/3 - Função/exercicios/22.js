function jurosCompostos (capital, taxa, tempo) {
    return capital * (1 + taxa) ** tempo
}

function anuidade (mes, valor) {
    let c = 0
    while ((mes + c) !== 12) {
        c += 1
    }
    return jurosCompostos(valor, 5, c)
}

console.log(anuidade(8, 2000))
