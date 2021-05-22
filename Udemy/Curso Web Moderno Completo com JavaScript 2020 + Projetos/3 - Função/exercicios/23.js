function formula (nota1, nota2, nota3) {
    const maior = Math.max(nota1,nota2, nota3)
    let media = 0
    if (maior === nota1) {
        media = (nota1 * 4 + nota2 * 3 + nota3 * 3)/ 7
    } else if (maior === nota2) {
        media = (nota2 * 4 + nota1 * 3 + nota3 * 3)/ 7
    } else if (maior === nota3) {
        media = (nota3 * 4 + nota2 * 3 + nota1 * 3)/ 7
    }

    return media
}

console.log(formula(7.5, 2.9, 10))