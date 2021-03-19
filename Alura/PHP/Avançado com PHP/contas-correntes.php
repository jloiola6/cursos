<?php

$conta1 = [
    'CPF' => '91726557200',
    'titular' => 'João Teixeira',
    'Saldo' => 1000
];

$conta2 = [
    'CPF' => '05515194870',
    'titular' => 'Jose´Ribeiro',
    'Saldo' => 4000
];

$conta3 = [
    'CPF' => '123456789',
    'titular' => 'Maricy Teixeira',
    'Saldo' => 2000
];
$contascorrentes = [$conta1, $conta2, $conta3];

echo $contascorrentes[0]['Saldo'];
