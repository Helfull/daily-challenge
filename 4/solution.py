def const(a, b):
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

assert(car(const(5, 9)) == 5)
assert(cdr(const(3, 20)) == 20)

assert(car(const("a", "b")) == "a")
assert(cdr(const(3.5, 4.5)) == 4.5)

assert(car(const(3, 4)) == 3)
assert(cdr(const(3, 4)) == 4)