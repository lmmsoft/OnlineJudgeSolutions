<?php

class Room {

    public $h, $len;

    public function __construct($a, $b, $h) {
        $this->h = $h;
        $this->len = 2 * ($a + $b);
    }

}

class Page {

    public $a, $b, $p;

    public function __construct($a, $b, $p) {
        $this->a = $a;
        $this->b = $b;
        $this->p = $p;
    }

}

function getPrice($room, $page) {
    $piece = (int) ($page->a / $room->h);
    if ($piece <= 0)
        return 99999999;
    $wide = $piece * $page->b;
    $rolls = ceil($room->len / $wide);
    return $rolls * $page->p;
}

$room = array();
$page = array();

fscanf(STDIN, "%d", $rooms);
for ($i = 0; $i < $rooms; ++$i) {
    fscanf(STDIN, "%d%d%d", $a, $b, $h);
    array_push($room, new Room($a, $b, $h));
}

fscanf(STDIN, "%d", $pages);
for ($i = 0; $i < $pages; ++$i) {
    fscanf(STDIN, "%d%d%d", $a, $b, $p);
    array_push($page, new Page($a, $b, $p));
}

$sum = 0;
foreach ($room as $rm) {
    $min = 99999999;
    foreach ($page as $pg) {
        $price = getPrice($rm, $pg);
        $min = min($price, $min);
    }
    $sum+=$min;
}
echo $sum;