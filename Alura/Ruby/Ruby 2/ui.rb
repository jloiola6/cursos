def boasvindas
    puts 'Bem vindo ao jogo da Forca'
    puts 'Qual é o seu nome? '
    nome = gets.strip
    puts "\n\n\n\nComeçaremos o seu jogo pra voce, #{nome}."
    nome
end

def avisaChute(chute)
    puts "Você já chutou #{chute}"
end

def avisaNaoEncontrada
    puts "Letra não encontrada."
end

def avisaEncontrada(totalEncontrado)
    puts "Letra encontrada #{totalEncontrado} vezes."
end

def desenhaForca(erros)
    cabeca = "   "
    corpo = " "
    pernas = "   "
    bracos = "   "
    if erros >= 1
        cabeca = "(_)"
    end
    if erros >= 2
        bracos = " | "
        corpo = "|"
    end
    if erros >= 3
        bracos = "\\|/"
    end
    if erros >= 4
        pernas = "/ \\"
    end

    puts "  _______       "
    puts " |/      |      "
    puts " |      #{cabeca}  "
    puts " |      #{bracos}  "
    puts " |       #{corpo}  "
    puts " |      #{pernas}  "
    puts " |              "
    puts "_|___           "
    puts

end

def avisaAcertou 
    puts "\nParabéns, você ganhou!"
        puts
        puts "       ___________      "
        puts "      '._==_==_=_.'     "
        puts "      .-\\:      /-.    "
        puts "     | (|:.     |) |    "
        puts "      '-|:.     |-'     "
        puts "        \\::.    /      "
        puts "         '::. .'        "
        puts "           ) (          "
        puts "         _.' '._        "
        puts "        '-------'       "
        puts
end

def avisaErrou
    puts 'Que pena.. Errou' 
end

def avisaPontos(pontosAteAgora)
    puts "Voce ganhou #{pontosAteAgora} pontos."
end

def avisaPalavraEscolhida(palavraSecreta)
    puts "Palavra secreta com #{palavraSecreta.size} letras... Boa sorte!" 
    palavraSecreta
end

def avisaEscolhendoPalavraSecreta
    puts 'Escolhendo uma palavra secreta...'
end

def naoQuerJogar
    puts 'Deseja jogar novamente? (S/N)'
    queroJogar = gets.strip
    queroJogar.upcase == 'N'
end

def cabecalhoTentativa(chutes, erros, mascara)
    puts "\n\n\n\n"
    desenhaForca(erros)
    puts "A palavra secreta é:  #{mascara}"
    puts "Erros até agora: #{erros}"
    puts "Chutes até agora: #{chutes}"
    puts "Entre com uma letra ou uma palavra"
end

def pedeChute
    chute = gets.strip.downcase #.downcase deixa toda a string minúscula
    puts "Será que acertou? Você chutou #{chute}"
    chute
end

def avisaPontosTotais(pontosTotais)
    puts "Você possui #{pontosTotais} pontos"
end

def avisaCampeaoAtual(dados)
    puts "Nosso campeão atual é #{dados[0]} com #{dados[1]} pontos."
end