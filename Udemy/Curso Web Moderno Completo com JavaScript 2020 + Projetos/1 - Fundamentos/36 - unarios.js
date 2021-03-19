let num1 = 1
let num2 = 2

num1++ // num1 = num1 + 1
console.log(num1)
--num1 // num1 = num1 - num1
console.log(num1)

// A ordem do sinal defini quando a operação será realizada, se ficar á esquerda ele fara a operação primeiro, se ficar á direita ele fara a operação só dps
console.log(++num1 === num2--) // Ele primeiro soma o num1, tornando 2 e dps compara com num2, assim o resultado irá dár "true" e só dps q irá somar +1 no num2
console.log(num1 == num2)