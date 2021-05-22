function bhaskara (a, b, c) {
    raizes = []
    delta = (b*b) - (4*a*c)
    if (delta === 0) {
        raiz1 = (-b + Math.sqrt(delta))/2
        raizes.push(raiz1)
    } else if (delta > 0) {
        raiz1 = (-b + Math.sqrt(delta))/2
        raiz2 = (-b - Math.sqrt(delta))/2
        raizes.push(raiz1)
        raizes.push(raiz2)
    } else {
        return "Delta Negativo"
    }
    return raizes
}

console.log(bhaskara(1, 8, -9))
console.log(bhaskara(7, 3, 4))