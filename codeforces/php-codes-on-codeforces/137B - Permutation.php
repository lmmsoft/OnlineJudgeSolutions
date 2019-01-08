<?php
$fr = fopen("php://stdin", "r");
$n = (int) fgets($fr);
$arr = fgets($fr);
fclose($fr);
$arr = explode(' ', $arr);
$ary = array();

foreach ($arr as $value) {
    $value2=(int)$value;
    $ary[$value2] = 1;
}
$cnt = 0;
for ($i = 1; $i <= $n; ++$i) {
    if ($ary[$i] == 1)
        $cnt++;
}
echo $n-$cnt;