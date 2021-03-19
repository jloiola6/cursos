<?php

function exibemensagem($mensagem){
    echo $mensagem . PHP_EOL;
}

 function sacar($conta, $valorasacar){
    if($valorasacar > $conta['Saldo']){
        exibemensagem('Voce não pode sacar esse valor');
    }else{
        $conta['Saldo'] -= $valorasacar;
    }
    return $conta;
    
 }

# Após o (:) voce decidira qual tipo de variavel será retornada pela função
 function depositar($conta, float $valoradepositar): array{
    if($valoradepositar <= 0){
        exibemensagem('Voce não pode depositar esse valor');
    }else{
        $conta['Saldo'] += $valoradepositar;
    }
    return $conta;
 }

 # As funcções em PHP passam um clone do q foi especificado por parametro, para passar a operação especificada de vdd usa-se o (&) para simbolzar uma referencia
 # para entender a diferença entre passagem de valor e de referencia
 # https://blog.penjee.com/wp-content/uploads/2015/02/pass-by-reference-vs-pass-by-value-animation.gif 
 function titularComLetrasMaiusculas(array &$conta){
     $conta['titular'] = mb_strtoupper($conta['titular']);
 }