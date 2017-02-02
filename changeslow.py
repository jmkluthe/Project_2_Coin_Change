#!/usr/bin/env python3


from functools import reduce
from math import inf


def changeslow(V, A):
    min = inf
    C = [0 for el in V]
    if A in V:
        C[V.index(A)] += 1
        return C, 1
    for i in range(1, A):
        to_i, to_i_len = changeslow(V, i)
        from_i, from_i_len = changeslow(V, A - i)
        if to_i_len + from_i_len < min:
            min = to_i_len + from_i_len
            C = [a + b for a, b in zip(to_i, from_i)]
    return C, min


V = [1, 5, 10]
A = 17
print(changeslow(V, A))
