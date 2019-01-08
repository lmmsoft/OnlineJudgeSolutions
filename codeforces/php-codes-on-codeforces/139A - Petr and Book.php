<?php
$fr = fopen("php://stdin", "r");
$n = (int) fgets($fr);
$arr = fgets($fr);
fclose($fr);
$arr = explode(' ', $arr);

$sum = 0;
for ($i = 0; $i < 7; $i+= 1) {
    $arr[$i] = (int) $arr[$i];
    $sum+=$arr[$i];
}
$mod = $n % $sum;
if($mod==0)
    $mod=$sum;
$sum2=0;
//echo $mod;
for ($i = 0; $i < 7; $i+= 1) {
    $sum2+=$arr[$i];
    if($sum2>=$mod)
        break;
}
echo $i+1;

?>