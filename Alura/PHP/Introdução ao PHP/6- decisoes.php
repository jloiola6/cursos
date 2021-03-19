
<?php
/* and == &&
or = || */

$idade = 15;
$numerodepessoas = 1;

echo "Você só pode entrar se tiver a partir de 18 anos ou a partir de 16 anos acompanhado" . PHP_EOL;

if ($idade >= 18){
    echo "Você tem $idade anos. Pode entrar sozinho";
}else{
    if ($idade >=16 && $numerodepessoas > 1){
        echo "Voce tem $idade anos e esta acampanhado(a), então pode entrar.";
    }else{
        echo "Voce só tem $idade anos. Voce não pode entrar" . PHP_EOL . "É uma pena...";
    }
}

echo PHP_EOL;
# Mensagem recebe um boolenao que vai retorna (?) para True e (:) para False
$mensagem = $idade < 18 ?"Você é menor de idade" : "Você é maior de idade";
echo $mensagem;

echo PHP_EOL;
echo "Adeus!";