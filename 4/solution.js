const assert = require('assert');

function cons(a, b)
{
    return function (f) {
        return f(a, b);
    };
}

function car(pair)
{
    return pair(function (a, b) {
        return a;
    })
}

function cdr(pair)
{
    return pair(function (a, b) {
        return b;
    })
}

assert(car(cons(5, 9)) == 5)
assert(cdr(cons(3, 20)) == 20)

assert(car(cons("a", "b")) == "a")
assert(cdr(cons(3.5, 4.5)) == 4.5)

assert(car(cons(3, 4)) == 3)
assert(cdr(cons(3, 4)) == 4)