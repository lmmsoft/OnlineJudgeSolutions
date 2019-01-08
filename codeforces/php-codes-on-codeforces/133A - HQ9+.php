<?php
fscanf(STDIN, "%s", $str);
echo preg_match("/[HQ9]/", $str, $matchesarray)?'YES':'NO';