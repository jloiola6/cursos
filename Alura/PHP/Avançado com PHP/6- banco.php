<?php
#Nos casos em que estamos

# incluindo arquivos OBRIGATÓRIOS, usamos a estrutura de linguagem require
require '7- funcoes.php';

#include já executa o arquivo selecionado e caso dê erro ele só dá um aviso, nunca um erro. Onclude é feit opara um arquivo que não é essencial para o programa
// include '7- funcoes.php';

#Para incluirmos um arquivo apenas se ele não tiver sido incluído anteriormente, ele verifica se o arquivo ja foi importado. Caso tenha sido incluido ele não faz nada
#require_once '7- funcoes.php'


$contascorrentes = [
    91726557200 => [
        'titular' => 'João Teixeira',
        'Saldo' => 1000
    ],
    123456789 => [
        'titular' => 'Vitor',
        'Saldo' => 300
    ],
    5515194870 => [
        'titular' => 'Ribeiro Loiola',
        'Saldo' => 5000
    ]
];

$contascorrentes[123456789] = sacar($contascorrentes[123456789], 200);
$contascorrentes[123456789] = depositar($contascorrentes[123456789], 200);

titularComLetrasMaiusculas($contascorrentes[123456789]);

#Exclui um elemneto da lista 
unset($contascorrentes[123456789]);

foreach($contascorrentes as $indice => $conta){
    // exibemensagem($indice . ' - '. $conta['titular'] . ': ' . $conta['Saldo']);
    
    # É usado ({}) no inicio e fim de váriaveis complexas, como essas nossa array associativa
    // exibemensagem("CPF: $indice - Titular: {$conta['titular']} - Saldo: {$conta['Saldo']}");
    
    
    # Utilizando a função de List. a váriavel pega o valor de acordo com a chave/indice dentro da array ($conta) 
    // list('titular' => $titular, 'Saldo' => $saldo) = $conta;
    
    # Outra forma de usar o List. 
    ['titular' => $titular, 'Saldo' => $saldo] = $conta;
    exibemensagem("CPF: $indice - Titular: $titular - Saldo: $saldo");
    
}

