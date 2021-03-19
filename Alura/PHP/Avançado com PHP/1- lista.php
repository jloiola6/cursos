<?php

#Primeira forma de se criar uma lista
$idadelista = array(21, 5 ,6 , 9, 82, 43);

#Segunda forma (igual ao Python) com ponto e vigula no final SEMPRE
$idadelista = [1, 2, 3, 4, 5];

#adicionando elemento no fim da lista
$idadelista[] = 7;

echo $idadelista[4] . PHP_EOL;

foreach($idadelista as $i){
    echo $i;
}