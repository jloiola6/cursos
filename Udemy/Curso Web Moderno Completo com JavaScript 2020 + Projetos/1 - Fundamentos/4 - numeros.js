const peso1 = 1.1
const peso2 = Number('2.0') // COnverte uma str para Number

console.log(peso1, peso2)
console.log(Number.isInteger(peso1)) // Verifica que se o valor é inteiro
console.log(Number.isInteger(peso2))

const avalicao1 = 9.871
const avalicao2 = 6.871

const total = avalicao1 * peso1 + avalicao2 * peso2
const media = total / (peso1, peso2)

console.log(media.toFixed(2)) // Retorna o resultado com os numeros de casas decimais passados por parametro
console.log(media.toString()) // Retorna o resultado em string
console.log(media.toString(2)) // Retorna o resultado em Number e binário, passando 2 como parametro.