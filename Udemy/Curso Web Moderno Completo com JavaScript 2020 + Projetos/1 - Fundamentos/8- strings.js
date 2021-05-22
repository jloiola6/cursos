const escola = "Cod3r"

console.log(escola.charAt(4)) // Retorna a letra de acordo com a posição passada por parametro
console.log(escola.charAt(5)) // O js Não retorna um erro caso a posição seja inválida
console.log(escola.charCodeAt(3)) // Ele retorna o valor de acordo com a posição passada por parametro na tabela ASCII
console.log(escola.indexOf('C')) // Retorna a posição do valor passado por parametro 

console.log(escola.substring(1)) // Retorna do indice 1 até o final
console.log(escola.substring(0, 3)) // retorna do indice 0 até o indice 2

console.log('Escola '. concat(escola).concat('!')) // Realizar Concatenação
console.log(escola.replace(3, 'e'))

console.log('Ana, Maria, Pedro'.split(',')) // Criando uma string e separando ela

