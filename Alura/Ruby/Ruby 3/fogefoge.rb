require_relative 'ui'

def leMapa(numero)
    texto = File.read("mapa#{numero}.txt")
    mapa = texto.split("\n")
end

def somaVetor(vetor1, vetor2)
    [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
end

def posicaoValidasMapa(mapa, novoMapa, posicao)
    posicoes = []
    movimentos = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
    movimentos.each do |movimento|
        novaPosicao = somaVetor(movimento, posicao)
        if posicaoValida?(mapa, novaPosicao) && posicaoValida?(novoMapa, novaPosicao)
            posicoes << novaPosicao
        end
    end
    posicoes
end

def copiaMapa(mapa)
    novoMapa = mapa.join("\n").tr("F", " ").split("\n") #Transformando tudo em uma string gigante com "\n" no final, depois ele altera os "F" por " " e no fim ele quebra a linha usando o "\n" como parametro.
end

def moveFantasma(mapa, novoMapa, linha, coluna)
    posicoes = posicaoValidasMapa(mapa, novoMapa, [linha, coluna])
    return if posicoes.empty? #Se as posições estiverem vazias ele para por alí
    aleatoria = rand(posicoes.size) #Um numero aleatorio entre 0 e o tamanho de elementos na array
    posicao = posicoes[aleatoria]
    mapa[linha][coluna] = " "
    novoMapa[posicao[0]][posicao[1]] = "F"
    
end

def moveFantasmas(mapa)
    fantasma = "F"
    novoMapa = copiaMapa(mapa)
    mapa.each_with_index do |linhaAtual, linha|
        linhaAtual.chars.each_with_index do |caracterAtual, coluna| #tranformamos em string para evitar erro
            trueFantasma = caracterAtual == fantasma
            if trueFantasma
                moveFantasma(mapa, novoMapa, linha, coluna)
            end
        end
    end
    novoMapa
end

def encontraJogador(mapa)
    heroi = "H"
    mapa.each_with_index do |linhaAtual, linha| # Pecorre cada elemneto de mapa e ler a sua linha atual, no caso o elemento atual.
        colunaHeroi = linhaAtual.index(heroi)
        if colunaHeroi
            return [linha, colunaHeroi]
        end
    end
    nil
end

def calculaNovaPosicao(heroi, direcao)
    heroi = heroi.dup #Cria um cópia do objeto para não interferir com a utilização do objeto dentro do jogo
    movimentos = { # Criando um dicionário
        "W" => [-1, 0],
        "S" => [+1, 0],
        "A" => [0, -1],
        "D" => [0, +1]
    }
    movimento = movimentos[direcao]
    heroi[0] += movimento[0]
    heroi[1] += movimento[1]
    heroi
end

def posicaoValida?(mapa, novaPosicao)
    linhas = mapa.size
    colunas = mapa[0].size
    estourouLinhas = novaPosicao[0] < 0 || novaPosicao[0] >= linhas
    estourouColunas = novaPosicao[1] < 0 || novaPosicao[1] >= colunas

    if estourouLinhas || estourouColunas  
        return false
    end
    valorAtual = mapa[novaPosicao[0]][novaPosicao[1]]
    if valorAtual == "X" || valorAtual == "F"# Se posição escolhida for um X ele só passa
        return false
    end
    return true
end

def jogo(nome)
    mapa = leMapa(2)
    while true
        desenhaMapa(mapa)
        direcao = pedeMovimento
        heroi = encontraJogador(mapa)
        novaPosicao = calculaNovaPosicao(heroi, direcao)
        if ! posicaoValida?(mapa, novaPosicao)
            next
        end
        mapa[heroi[0]][heroi[1]] = " "
        mapa[novaPosicao[0]][novaPosicao[1]] = "H"
        mapa = moveFantasmas(mapa)  
        if !encontraJogador(mapa)  #Se o jogador estiver sido morto 
            gameOver
            break
        end  
    end
end

def iniciaFogeFoge
    nome = boasVindas
    jogo(nome)
end