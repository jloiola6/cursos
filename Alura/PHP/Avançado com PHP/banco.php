<?php
#Nos casos em que estamos
# incluindo arquivos obrigatórios, usamos a estrutura de linguagem require
require 'funcoes.php';
// include 'funcoes.php';

#Para incluirmos um arquivo apenas se ele não tiver sido incluído anteriormente, 
#podemos utilizar o require_once





// function adiciona2($x){
//     return $x + 2;
// }

// $sete = adiciona2(5);

// exibemensagem($sete);

// function exibeolamundo(){
//     echo 'Olá Mundo' . PHP_EOL;
// }

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
#retirando 500 reais do saldo na conta do indice indicado
// $contascorrentes[91726557200]['Saldo'] -= 500;
// if(500 > $contascorrentes[123456789]['Saldo']){
//     exibemensagem('Voce não pode sacar esse valor');
// }else{
//     $contascorrentes[123456789]['Saldo'] -= 500;
// }

// $contascorrentes[123456789] = sacar($contascorrentes[123456789], 299);
$contascorrentes[123456789] = depositar($contascorrentes[123456789], 12300);

foreach($contascorrentes as $indice => $conta){
    // exibemensagem($indice . ' - '. $conta['titular'] . ': ' . $conta['Saldo']);
    exibemensagem("CPF: $indice - Titular: {$conta['titular']} - Saldo: {$conta['Saldo']}");
}

