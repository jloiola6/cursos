function novoSalario(plano, salario) {
    switch (plano) {
    case "A":
        console.log(salario + (salario*0.10))
        break
    case "B":
        console.log(salario + (salario*0.15))
        break
    case "C":
        console.log(salario + (salario*0.20))
        break
    default:
        console.log("Plano inválido")
    }
}

novoSalario("A", 2534)