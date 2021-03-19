let isAtivo = false
console.log(isAtivo)

isAtivo = true
console.log(isAtivo)

isAtivo = 1
console.log(!!isAtivo) // ! representa negação, ou seja, ! == not
console.log(!isAtivo)

console.log('Os verdadeiros...') // Todos os numeros inteiros são verdadeiros, com excessão do 0.
console.log(!!3)
console.log(!!-1)
console.log(!!' ')
console.log(!!'teste')
console.log(!![])
console.log(!!{})
console.log(!!Infinity)
console.log(!!(isAtivo == true))

console.log('Os falsos...')
console.log(!!0)
console.log(!!'')
console.log(!!null)
console.log(!!NaN)
console.log(!!undefined)
console.log(!!(isAtivo = false))

console.log('Para finalizar...')
console.log('' || null || 0 || 'teste') // usando o or...

let nome = ''
console.log(nome || 'Desconhecido') // Se tiver nome ele retorna o nome, caso o o nome for false ele retorna o 'Desconhecido'. Tudo usso usando o or (sem if)


