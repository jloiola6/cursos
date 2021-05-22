function util(dia) {
    switch (dia) {
    case 1: case 7:
        console.log("Fim de Semana")
        break
    case 2: case 3: case 4: case 5: case 6:
        console.log("Dia Útil")
        break
    default:
        console.log("Dia Inválido")
    }
}

util(5)