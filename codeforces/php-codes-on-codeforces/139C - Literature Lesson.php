<?php

function regex($param, $k) {
    $pattern = "/([^aeiou]*?[aeiou]){" . $k . "}/";
    preg_match($pattern, $param, $match);
    return $match[0];
}

$fr = fopen("php://stdin", "r");
$arr = fgets($fr);
$arr = explode(' ', $arr);
$n = (int) $arr[0];
$k = (int) $arr[1];

$flag = FALSE;
for ($i = 0; $i < 4 * $n; ++$i) {
    $str[$i] = fgets($fr);
    $str[$i] = strrev($str[$i]);
    $str[$i] = regex($str[$i], $k);
    //Æ¥ÅäÊ§”¡
    if ($str[$i] == NULL) {
        $flag = TRUE;
        break;
    }
}
if ($flag) {
    die("NO\n");
}

//$str_ans = array();
$aaaa = FALSE;
$aabb = FALSE;
$abab = FALSE;
$abba = FALSE;
$no = FALSE;

$cnt_aaaa = 0;
for ($i = 0; $i < $n; ++$i) {
    if ($str[$i * 4] == $str[$i * 4 + 1] && $str[$i * 4] == $str[$i * 4 + 2] && $str[$i * 4] == $str[$i * 4 + 3]) {
//        $str_ans[] = "aaaa";
        $cnt_aaaa++;
        $aaaa = TRUE;
    } elseif ($str[$i * 4] == $str[$i * 4 + 1] && $str[$i * 4 + 2] == $str[$i * 4 + 3]) {
//        $str_ans[] = "aabb";
        $aabb = TRUE;
    } elseif ($str[$i * 4] == $str[$i * 4 + 2] && $str[$i * 4 + 1] == $str[$i * 4 + 3]) {
//        $str_ans[] = "abab";
        $abab = TRUE;
    } elseif ($str[$i * 4] == $str[$i * 4 + 3] && $str[$i * 4 + 1] == $str[$i * 4 + 2]) {
//        $str_ans[] = "abba";
        $abba = TRUE;
    } else {
        $no = TRUE;
    }
}

if ($no)
    echo "NO\n";
elseif (!$aabb && !$abab && $abba) {
    echo "abba\n";
} elseif (!$aabb && $abab && !$abba) {
    echo "abab\n";
} elseif ($aabb && !$abab && !$abba) {
    echo "aabb";
} elseif ($aaaa && $cnt_aaaa == $n) {
    echo "aaaa";
} else {
    echo "NO\n";
}
?>