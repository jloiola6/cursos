def boasVindas
    puts 'Bem vindo ao Foge-Foge'
    puts 'Qual o seu nome? '
    nome = gets.strip
    puts "\n\n\n\n\n\n"
    puts "Começaremos o jogo para você, #{nome}" 
    nome
end

def desenhaMapa(mapa)
    puts mapa
end

def pedeMovimento
    puts 'Para onde deseja ir? '
    movimento = gets.strip
end

def gameOver
    puts "\n\n\n\n\n\n\nGAME OVER!!!"
end