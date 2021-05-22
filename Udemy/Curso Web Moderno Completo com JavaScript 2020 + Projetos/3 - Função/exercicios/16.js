function calculadora(a, operador ,b) {
    switch (operador) {
    case "+":
        console.log(`${a} + ${b} = ${a+b}`)
        break
    case "-":
        console.log(`${a} - ${b} = ${a-b}`)
        break
    case "*":
        console.log(`${a} * ${b} = ${a*b}`)
        break
    case "/":
        console.log(`${a} * ${b} = ${a/b}`)
        break
    default:
        console.log("Não trabalhamos com este tipo de calculo")
    }
}

calculadora(2, "+", 2)