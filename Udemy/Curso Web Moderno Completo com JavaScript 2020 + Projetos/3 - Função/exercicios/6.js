function jurosSimples (capital, taxa, tempo) {
    return capital + (capital * taxa * tempo)
}

function jurosCompostos (capital, taxa, tempo) {
    return capital * (1 + taxa) ** tempo
}

console.log(jurosCompostos(2000, 10, 4).toFixed(2))
console.log(jurosSimples(2000, 43, 7).toFixed(2))