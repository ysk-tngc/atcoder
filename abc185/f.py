# -*- coding: utf-8 -*-
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    T, X, Y = [], [], []
    for _ in range(Q):
        Ti, Xi, Yi = map(int, input().split())
        T.append(Ti)
        X.append(Xi)
        Y.append(Yi)

    for i in range(Q):
        if T[i] == 1:
            A[X[i] - 1] = A[X[i] - 1] ^ Y[i]
        else:
            print(exor_rec(A[X[i]-1:Y[i]]))


def exor_rec(items):
    return reduce(exor, items)


def exor(a, b):
    return a ^ b


if __name__ == '__main__':
    main()
