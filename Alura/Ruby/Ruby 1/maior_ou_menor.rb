def boas_vindas
    puts
    puts "        P  /_\\  P                              "
    puts "       /_\\_|_|_/_\\                             "
    puts "   n_n | ||. .|| | n_n         Bem vindo ao    "
    puts "   |_|_|nnnn nnnn|_|_|     Jogo de Adivinhação!"
    puts "  |' '  |  |_|  |'  ' |                        "
    puts "  |_____| ' _ ' |_____|                        " 
    puts "        \\__|_|__/                              "
    puts
    puts 
    puts 'bem vindo'
    puts "Qual é o seu nome?\n"
    nome = gets.strip #Limpar caracters brancos antes e depois da variavel 
    puts "Começaremos o jogo para voce, " + nome
    nome
end

def ganhou
    puts
    puts "             OOOOOOOOOOO               "
    puts "         OOOOOOOOOOOOOOOOOOO           "
    puts "      OOOOOO  OOOOOOOOO  OOOOOO        "
    puts "    OOOOOO      OOOOO      OOOOOO      "
    puts "  OOOOOOOO  #   OOOOO  #   OOOOOOOO    "
    puts " OOOOOOOOOO    OOOOOOO    OOOOOOOOOO   "
    puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  "
    puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  "
    puts "OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO  "
    puts " OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO   "
    puts "  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO    "
    puts "    OOOOO   OOOOOOOOOOOOOOO   OOOO     "
    puts "      OOOOOO   OOOOOOOOO   OOOOOO      "
    puts "         OOOOOO         OOOOOO         "
    puts "             OOOOOOOOOOOO              "
    puts
    puts "               Acertou!                "
    puts
end

def pedeDificuldade
    puts 'Qual o nível de dificuldade que deseja? (1 fácil, 5 dificil)'
    dificuldade = gets.to_i
end

def sorteio(dificuldade)
    case dificuldade  #Sintaxe do case (como se fosse um elif).
    when 1
        maximo = 30
    when 2
        maximo = 60
    when 3
        maximo = 100
    when 4
        maximo = 150
    else 
        maximo = 200
    end
    puts "\nEscolhendo um número entre 1 e #{maximo}..\n"
    sorteado = rand(maximo) + 1 #função para reotornar um numero aleatório entre 0 e 200.
    puts "Escolhido... que tal advinhar hoje nosso número secreto?\n"
    sorteado #Não é necessário usar o "return" pois ele retorna o valor 
end

def pede_numero(chutes, tentaiva, limite_de_tentativa) 
    puts "\n\nTentaiva #{tentaiva} de #{limite_de_tentativa}" #Interpolação de String
    puts "Chutes até agora: #{chutes}"
    chute = gets.strip
    puts "\nSerá que acertou? Voce chutou: #{chute}" #Interpolação de String
    # puts chute.to_i == 175 # Usa-se o ".to_i" para converter uma variável str em int
    chute
end

def verifica_se_acertou(numero_secreto, chute)
    acertou = numero_secreto == chute.to_i
    if acertou 
        ganhou
        return true #Retornando True
    end

    maior = numero_secreto > chute.to_i
    if maior
        puts "O numero Secreto é maior!"
    else
        puts "O numero Secreto é menor!"
    end
    
end

def joga(nome, dificuldade)
    numero_secreto = sorteio(dificuldade)
    pontos = 1000

    chutes = [] # Criei lista
    # totalChutes = 0

    limite_de_tentativa = 5
    ultimoEscolhido = -1
    for tentaiva in 1..limite_de_tentativa
        chute = pede_numero(chutes, tentaiva, limite_de_tentativa) #NÃO É OBRIGADO A USAR O PARENTESES
        # chutes[totalChutes] =  chute #adicionando o chute na lista
        chutes <<  chute #adicionando o chute na ultima posição da lista
        # puts chutes.size #mostra quantos elementos tem na array
        # totalChutes += 1
        if nome == 'Joao'
            ganhou
            break
        end
        pontosPerdidos = (chute.to_i - numero_secreto).abs / 2.0 #.abs retorna o valor absoluto do numero, sem sinal
        pontos -= pontosPerdidos

        break if verifica_se_acertou(numero_secreto, chute) # SE RETORNAR VERDADE ELE IRA FAZER UM BREAK
    end

    puts "Voce ganhou #{pontos} pontos."
end

def querJogar
    puts 'Deseja jogar novamente? (S/N)'
    queroJogar = gets.strip
    queroJogar.upcase == 'S' #retornando se for vdd e transformando em maiusculo
end

nome = boas_vindas
dificuldade = pedeDificuldade

# while querJogar #ele execita primeiro a condição para dps oq esta dentro
loop do #Executa eternamente 
    joga(nome,dificuldade)
    if !querJogar # usa-se o ! como not. EM ruby é comum usar um ponto de interrogação quando a funçaõ retornar um booleano.
        break
    end
end
