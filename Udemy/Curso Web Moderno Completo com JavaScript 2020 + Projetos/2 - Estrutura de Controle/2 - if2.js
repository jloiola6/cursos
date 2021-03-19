function teste1(num) {
    if (num > 7) // Caso só tenha uma linha a ser executada
        console.log(num)
    console.log('Final')
}

teste1(6)
teste1(8)

function teste2(num) {
    if (num > 7); // Cuidado com o ";" pois ele considerará que o ";" é o fim de um bloco de código.
        console.log(num)
    console.log('Final')
}

teste2(6)
teste2(8)