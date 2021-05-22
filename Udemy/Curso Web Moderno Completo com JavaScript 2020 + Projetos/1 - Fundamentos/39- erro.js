function tratarErroELancar(erro) {
    // throw new Error('...')
    // throw 10
    // throw true
    // throw 'Mensagem'
    throw {
        nome: erro.name,
        msg: erro.message,
        date: new Date
    }

}

function imprimirNomeGritando(obj) {
    try{ // Tentará executar o bloco de código dentro do try
        console.log(obj.name.toUpperCase() + '!!!!') // Estamos acessando uma chave que não existe... no caso "name"
    } catch (e) { // Caso ocorra um erro ele executará o bloco de código dentro do cath
        tratarErroELancar(e)
    } finally { // E finalemnte, idependente se ocorreu erro ou não, ele executará o bloco dentro do finally
        console.log('Final')
    }
}

const obj = { name: 'Roberto' } // NOte que foi criado a chave "nome"
imprimirNomeGritando(obj)