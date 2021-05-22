let dobro = function (a) {
    return 2 * a
}

dobro = (a) => {
    return 2 * a
}

dobro = a => 2 * a // Return esta implícito
console.log(dobro(Math.PI))

let ola = function () {
    return "Olá"
}

ola = () => 'Olá'
ola = _ => 'Olá' // Outra forma qunado não possui parametros