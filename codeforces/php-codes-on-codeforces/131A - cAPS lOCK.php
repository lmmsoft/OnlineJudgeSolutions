<?php
$input = trim(fgets(STDIN));
if(preg_match('/^([A-Z]+$)/', $input))
    echo strtolower($input);
else if (preg_match('/^([a-z]{1})([A-Z]*$)/', $input))
    echo strtoupper($input[0]).strtolower(substr($input, 1));
else
    echo $input;