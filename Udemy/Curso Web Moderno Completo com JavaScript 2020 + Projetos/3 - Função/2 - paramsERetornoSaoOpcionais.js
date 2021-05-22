function area (largura, altura) {
    const area = largura * altura
    if (area > 20) {
        console.log(`Valor acima do permitido: ${area}m2.`)
    } else {
        return area
    }
}

console.log(area(2, 2))
console.log(area(2)) // NAN
console.log(area()) // NAN
console.log(area(2, 2, 4, 54, 9)) // Só faz o caluculo dos 2 primeiros parametros
console.log(area(5, 5))