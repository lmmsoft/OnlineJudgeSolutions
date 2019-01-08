<?php
fscanf(STDIN, "%s", $str);
echo preg_match_all("/(C{1,5})|(P{1,5})/", $str, $matchesarray);