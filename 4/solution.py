def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)

assert(car(cons(5, 9)) == 5)
assert(cdr(cons(3, 20)) == 20)

assert(car(cons("a", "b")) == "a")
assert(cdr(cons(3.5, 4.5)) == 4.5)

assert(car(cons(3, 4)) == 3)
assert(cdr(cons(3, 4)) == 4)