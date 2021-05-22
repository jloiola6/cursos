function triangulo (a, b, c) {
    if (a === b && a === c) {
        console.log("Equilátero")
    } else if (a !== b && a !== c && b !== c){
        console.log("Escaleno")
    } else {
        console.log("Isóceles")
    }
}

triangulo(5,5,5)
triangulo(4,5,5)
triangulo(5,4,6)