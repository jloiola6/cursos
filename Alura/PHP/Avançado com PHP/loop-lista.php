<?php

$idadelista = [21, 23, 19, 25, 30, 41, 18];

for($i = 0; $i < 7; $i++){
    echo $idadelista[$i];
    echo PHP_EOL;
}

#O count conta quantos elementos tem na lista (equivalente ao len() no python)
echo PHP_EOL;
echo count($idadelista).PHP_EOL;
echo PHP_EOL;

for($i = 0; $i < count($idadelista); $i++){
    echo $idadelista[$i].PHP_EOL;
}