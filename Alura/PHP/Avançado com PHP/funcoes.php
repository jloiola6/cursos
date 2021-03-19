
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

 function depositar($conta, float $valoradepositar): array{
    if($valoradepositar <= 0){
        exibemensagem('Voce não pode depositar esse valor');
    }else{
        $conta['Saldo'] += $valoradepositar;
    }
    return $conta;
 }