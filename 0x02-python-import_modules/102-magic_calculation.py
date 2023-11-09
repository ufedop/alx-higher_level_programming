#!/usr/bin/python3
def magic_calculation(e, f):
    from magic_calculation_102 import add, sub
    if e < f:
        g = add(a, b)
        for i in range(4, 6):
            g = add(g, i)
        return g
    else:
        return (sub(e, f))

