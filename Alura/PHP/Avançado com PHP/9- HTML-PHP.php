<?php

require '10- funcoes-HTML-PHP.php';

$contascorrentes = [
    91726557200 => [
        'titular' => 'João Teixeira',
        'Saldo' => 1000
    ],
    123456789 => [
        'titular' => 'Vitor',
        'Saldo' => 300
    ],
    5515194870 => [
        'titular' => 'Ribeiro Loiola',
        'Saldo' => 5000
    ]
];

$contascorrentes[123456789] = sacar($contascorrentes[123456789], 200);
$contascorrentes[123456789] = depositar($contascorrentes[123456789], 200);

titularComLetrasMaiusculas($contascorrentes[123456789]);

unset($contascorrentes[123456789]);


// echo "<ul>";

// foreach($contascorrentes as $cpf => $conta){
//     exibirConta($conta);
// }

// echo "</ul>";

?>


<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
            content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>Contas correntes</h1>

        <dl>
        <?php foreach($contascorrentes as $cpf => $conta) { ?>
            <dt>
                <h3><?php echo $conta['titular']; ?> - <?php echo $cpf; ?></h3>
            </dt>
            <dd>
                <!-- Segundo modo!!! -->
                Saldo: <?= $conta['Saldo']; ?>
            </dd>
        <?php } ?>
        </dl>
    </body>
</html>

