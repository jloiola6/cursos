<?php
$altura = 1.74;
$peso = 120;
$resultado_imc = $peso/($altura ** 2);

echo "Seu peso é: $peso" . PHP_EOL;
echo "Sua altura é: $altura" . PHP_EOL;
echo "Seu IMC é: $resultado_imc" . PHP_EOL;

if($resultado_imc < 18.5){
    echo "Voce esta abaixo do peso";
    }elseif($resultado_imc < 25){
        echo "Voce esta no peso";
    }else{
        echo "Voce esta acima do peso";
    }
