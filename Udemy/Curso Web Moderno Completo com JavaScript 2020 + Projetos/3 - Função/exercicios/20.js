function notas(valor) {
    let reais100 = 0
    let reais50 = 0
    let reais10 = 0
    let reais5 = 0
    let reais1 = 0
    while (valor > 0){
        if (valor-100 >= 0) {
            reais100 += 1
            valor -= 100
        } else if (valor-50 >= 0) {
            reais50 += 1
            valor -= 50
        } else if (valor-10 >= 0) {
            reais10 += 1
            valor -= 10
        } else if (valor-5 >= 0) {
            reais5 += 1
            valor -= 5
        } else if (valor-1 >= 0) {
            reais1 += 1
            valor -= 1
        }
    }

    let resultado = ''
    if (reais100> 0) {
        resultado += `${reais100} nota(s) de R$ 100. \n`
    }
    if (reais50 > 0) {
        resultado += `${reais50} nota(s) de R$ 50. \n`
    }
    if (reais10 > 0) {
        resultado += `${reais10} nota(s) de R$ 10. \n`
    }
    if (reais5 > 0) {
        resultado += `${reais5} nota(s) de R$ 5. \n`
    }
    if (reais1 > 0) {
        resultado += `${reais1} nota(s) de R$ 1. `
    }

    return resultado
}

console.log(notas(532))