def salvarRank(nome, pontosTotais)
    conteudo = "#{nome}\n#{pontosTotais}"
    File.write('rank.txt', conteudo) #cria e sobrescreve um arquivo
end

def leRank
    conteudo = File.read('rank.txt')
    conteudo.split "\n"
end