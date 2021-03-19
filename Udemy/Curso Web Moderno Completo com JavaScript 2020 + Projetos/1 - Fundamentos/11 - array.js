const valores = [7.7 ,8.9, 6.3, 9.2]

console.log(valores[0], valores[3])
console.log(valores[4]) // Retorna Undefined pois não existe

valores[4] = 10
console.log(valores)

valores[10] = 10 // Ele cria um espaço vazio na array 
console.log(valores)

console.log(valores.length) 

valores.push({id: 3}, false, true, 'teste') // Adiciona dados na array (seria o append no python)
console.log(valores)

console.log(valores.pop()) // remove o ultimo elemento e retorna qual foi o mesmo
delete valores[0]
console.log(valores)

console.log(typeof valores)