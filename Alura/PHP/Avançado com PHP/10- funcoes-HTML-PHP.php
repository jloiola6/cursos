<?php

function exibemensagem($mensagem){
    echo $mensagem . '<br>';
}

 function sacar($conta, $valorasacar){
    if($valorasacar > $conta['Saldo']){
        exibemensagem('Voce não pode sacar esse valor');
    }else{
        $conta['Saldo'] -= $valorasacar;
    }
    return $conta;
    
 }

 function depositar($conta, float $valoradepositar): array{
    if($valoradepositar <= 0){
        exibemensagem('Voce não pode depositar esse valor');
    }else{
        $conta['Saldo'] += $valoradepositar;
    }
    return $conta;
 }

 function titularComLetrasMaiusculas(array &$conta){
     $conta['titular'] = mb_strtoupper($conta['titular']);
 }

 function exibirConta(array $conta){
     list('titular' => $titular, 'saldo' => $saldo) = $conta;
    // $html = "<li>Titular: $conta[titular]. Saldo: {$conta['saldo']}</li>";
    $html = "<li>Titular: $titular. Saldo: $saldo</li>";
    echo $html;
 }
