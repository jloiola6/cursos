<?php

#Não façam um array desse jeito!

#https://www.php.net/manual/pt_BR/language.types.array.php
$array = [
    1 => 'a',
    '1' => 'b', #String com inteiros válidos serão convertidos para inteiros 
    1.5 => 'c', #Float com inteiros válidos serão convertidos para inteiros 
    True => 'd' # Booleno será convertido para (1) se for True e (0) se for False
];

foreach($array as $i){
    echo $i . PHP_EOL;
}