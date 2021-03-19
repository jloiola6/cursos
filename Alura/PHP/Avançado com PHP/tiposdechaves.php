<?php

$array = [
    1 => 'a',
    '1' => 'b',
    1.5 => 'c',
    True => 'd'
];

foreach($array as $i){
    echo $i . PHP_EOL;
}