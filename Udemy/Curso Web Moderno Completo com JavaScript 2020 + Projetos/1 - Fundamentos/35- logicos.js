function compras(trabalho1, trabalho2){
    const comprarSorvete = trabalho1 || trabalho2 // No js o or == || 
    const comprarTv50 = trabalho1 && trabalho2 // No js o and == &&
    const comprarTv32 = trabalho1 != trabalho2
    const manterSaudavel = !comprarSorvete // Operador unário (negação lógica)

    return { comprarSorvete, comprarTv50, comprarTv32, manterSaudavel }
}

console.log(compras(true, true))
console.log(compras(true, false))
console.log(compras(false, true))
console.log(compras(false, false))
