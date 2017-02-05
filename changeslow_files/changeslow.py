#!/usr/bin/env python3

from math import inf


def changeslow(V, A):
    min = inf
    C = [0]*len(V)
    if A in V:
        C[V.index(A)] += 1
        return C
    for i in range(1, A):
        to_i = changeslow(V, i)
        from_i = changeslow(V, A - i)
        num_coins = sum(to_i + from_i)
        if num_coins < min:
            min = num_coins
            C = [a + b for a, b in zip(to_i, from_i)]
    return C


