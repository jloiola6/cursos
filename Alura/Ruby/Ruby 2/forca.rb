require_relative 'ui'
require_relative 'rank'

# def conta(palavraSecreta, letraProcurada)
#     for i in palavraSecreta.chars #transformar uma string em um array de caracteres
#         if i == letraProcurada
#             totalEncontrado += 1
#         end
#     end
#     totalEncontrado
# end 

def escolhePalavra
    avisaEscolhendoPalavraSecreta
    texto = File.read("dicionario.txt")
    todasAsPalavras = texto.split("\n")
    numeroEscolhido = rand(todasAsPalavras.size)
    palavraSecreta = todasAsPalavras[numeroEscolhido].downcase #Deixa as letras minusculas
    avisaPalavraEscolhida(palavraSecreta)
end

def escolhePalavra2
    avisaEscolhendoPalavraSecreta
    arquivo = File.new('dicionario.txt')
    quantidadeDePalavras = arquivo.gets.to_i #Lê a primeira linha do arquivo e a transforma em inteiro
    numeroEscolhido = rand(quantidadeDePalavras)
    for i in 1..(numeroEscolhido - 1)
        arquivo.gets
    end
    palavraSecreta = arquivo.gets.strip.downcase #Deixa as letras minusculas
    arquivo.close
    avisaPalavraEscolhida(palavraSecreta)
    
end

def pedeChuteValido(chutes, erros, mascara)
    cabecalhoTentativa(chutes, erros, mascara)
    loop do
        chute = pedeChute
        if chutes.include? chute #verifica se o chute esta incluso na lista
            avisaChute(chute)
        else
            return chute
        end
    end
end

def palavraMacarada(chutes, palavraSecreta)
    mascara = ""
    for i in palavraSecreta.chars
        if chutes.include? i
            mascara << i
        else
            mascara << "_"
        end
    end
    mascara
end


def joga(nome)
    palavraSecreta = escolhePalavra
    erros = 0
    chutes = []
    pontosAteAgora = 0

    while erros < 5
        mascara = palavraMacarada(chutes, palavraSecreta)
        chute  = pedeChuteValido(chutes, erros, mascara)
        chutes << chute

        chutouUmaLetra = chute.size == 1
        if chutouUmaLetra
            letraProcurada = chute
            # totalEncontrado = conta(palavraSecreta, letraProcurada)
            totalEncontrado = palavraSecreta.count(letraProcurada) # Ele conta quantas vezes o caractere, passado por parametro, se repete na string e retorna o resultado
            if totalEncontrado == 0
                avisaNaoEncontrada
                erros += 1
            else
                avisaEncontrada(totalEncontrado)
            end
        else
            acertou = chute == palavraSecreta
            if acertou
                avisaAcertou 
                pontosAteAgora += 1000
                break
            else
                avisaErrou
                pontosAteAgora -= 30
                erros += 1
            end
        end
    end
    avisaPontos(pontosAteAgora)
    pontosAteAgora
end

def jogoDaForca
    nome = boasvindas
    pontosTotais = 0

    avisaCampeaoAtual(leRank)

    loop do
        pontosTotais += joga(nome)
        avisaPontosTotais(pontosTotais)
        if leRank[1].to_i < pontosTotais
            salvarRank(nome, pontosTotais)
        end
        if naoQuerJogar
            break
        end
    end
end

