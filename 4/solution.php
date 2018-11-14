<?php

function lowest($input)
{
    sort($input);

    $last = null;

    foreach ($input as $number) {

        if ($number <= 0)
        {
            continue;
        }

        if ($last + 1 !== $number)
        {
            return $last + 1;
        }

        $last = $number;
    }

    return $last + 1;
}

assert(lowest([3, 4, -1, 1]) === 2);
assert(lowest([1, 2, 0]) === 3);
