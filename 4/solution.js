const assert = require('assert');

function lowest(input)
{
    input = input.sort();

    last = null;

    for(numberIndex in input) {
        number = input[numberIndex];
        if (number <= 0)
        {
            continue;
        }

        if (last + 1 != number)
        {
            return last + 1;
        }

        last = number;
    }

    return last + 1;
}


assert(lowest([3, 4, -1, 1]) === 2)
assert(lowest([1, 2, 0]) === 3)
