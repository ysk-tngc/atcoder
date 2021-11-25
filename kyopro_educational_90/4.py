# -*- coding: utf-8 -*-
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        a = list(map(int, input().split()))
        A.append(a)

    B = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            for k in range(H):
                B[i][j] += A[k][j]
            for k in range(W):
                B[i][j] += A[i][k]
            B[i][j] -= A[i][j]

    for b in B:
        print(*b)


if __name__ == '__main__':
    main()
