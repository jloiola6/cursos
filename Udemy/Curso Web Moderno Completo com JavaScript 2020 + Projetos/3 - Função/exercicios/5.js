function pontuacao (valor) {
    console.log(`R$${valor.toFixed(2)}`.replace('.',','))
}

pontuacao(0.30000000000000004)