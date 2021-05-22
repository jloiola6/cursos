function pontuacao (valores) {
    lista = valores.split(" ")
    base = parseInt(lista[0])
    menor = base
    contador = 0

    for (let i = 1; i < lista.length; i++) {
        if (parseInt(lista[i]) > base) {
            base = (parseInt(lista[i]))
            contador += 1
        } else if (parseInt(lista[i]) < menor) {
            menor = parseInt(i-1)
        }
    }

    return [contador, menor]
}

console.log(pontuacao("10 20 20 8 25 3 0 30 1"))