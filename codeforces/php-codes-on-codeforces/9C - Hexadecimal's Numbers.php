<?php
$fr = fopen("php://stdin", "r");
$max = (int) fgets($fr);
//fclose($fr);

function solution() {
    global $st;
    global $max;
    $nr = (int) $st;
    return ( ($nr > 0) && ($nr <= $max) );
}

function back($k) {
    global $n;
    global $st;
    if ($k >= $n) {
        if (solution())
            return 1;
        else
            return 0;
    }
    $sol = 0;
    if ($st[$k] == ' ') {
        $st[$k] = '0';
        $sol+= back($k + 1);
    }
    if ($st[$k] == '0') {
        $st[$k] = '1';
        $sol+= back($k + 1);
    }
    $st[$k] = ' ';
    return $sol;
}

$n = strlen($max);
$st = str_repeat(' ', $n);
echo back(0);
?>