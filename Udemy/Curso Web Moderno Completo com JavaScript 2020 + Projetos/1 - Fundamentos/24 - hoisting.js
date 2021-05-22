// Hoisting é um conceito padrãoo de mover a declaração para o topo, evitando assim erros....
console.log('a =', a)
var a = 2
console.log('a =', a)

// O hoisting não é aplicado com variáveis criadas em let...
console.log('b =', b)
let b = 2
console.log('b =', b)
