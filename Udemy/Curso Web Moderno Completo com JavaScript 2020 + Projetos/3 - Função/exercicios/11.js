function bisexto (ano) {
    resultado = false
    if (ano%4 === 0 && ano%100 !== 0 || ano%400 === 0){
        return true
    } else {
        return false
    }
}

console.log(bisexto(2021))