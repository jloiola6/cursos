<?php
#o indice não pode começar com zero!!!
$contascorrentes = [
    91726557200 => [
        'titular' => 'João Teixeira',
        'Saldo' => 1000
    ],
    123456789 => [
        'titular' => 'Vitor',
        'Saldo' => -11
    ],
    5515194870 => [
        'titular' => 'Ribeiro Loiola',
        'Saldo' => 5000
    ]
];

foreach($contascorrentes as $indice => $conta){
    echo $indice . PHP_EOL;
}

#Adicionando dados a lista informando o indice
$contascorrentes[987654321] = [
    'titular' => 'Maricy Teixeira',
    'Saldo' => 3000
];

echo PHP_EOL;
foreach($contascorrentes as $indice => $conta){
    echo $indice . PHP_EOL;
}

#Adicionando dados a lista sem informar o indice, ou seja, na ultima posição
#Ele pega o maior indice e add +1
$contascorrentes[] = [
    'titular' => 'Thaís',
    'Saldo' => 3000
];

echo PHP_EOL;
foreach($contascorrentes as $indice => $conta){
    echo $indice . ': '. $conta['titular'] . PHP_EOL;
}