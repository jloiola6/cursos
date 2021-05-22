function formula (nota) {
    if (nota < 40 && nota < 38) {
        return console.log(`Sua nota é ${nota}! Voce esta reprovado!!`)
    } else {
        mult = 5
        c = 1
        while (mult <= nota) {
            c += 1
            mult = 5 * c
        }

        if ((mult - nota) <= 2) {
            nota = mult
            return console.log(`Sua nota é ${nota}!`)
        }
    }
}

formula(37)