<?php

$input = [2, 4, 6, 8, 10, 2, 6, 10];

$output = [4, 8];

function findSingles($in) {
    $out = [];
    foreach ($in as $i) {
        $out[$i] = ($out[$i] ?? 0) + 1;
    }

    return array_keys(array_filter($out, function ($count) {
        return $count === 1;
    }));
}

echo json_encode(findSingles($input));
