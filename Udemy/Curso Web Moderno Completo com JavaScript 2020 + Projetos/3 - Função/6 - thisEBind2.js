function Pessoa() {
    this.idade = 0

    const self =  // Driblando o this
    setInterval(function() {
        this.idade++
        console.log(self.idade)
    }/*.bind(this)*/, 1000)
}

new Pessoa