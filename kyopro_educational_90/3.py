# -*- coding: utf-8 -*-
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = []
    B = []
    for i in range(1, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(N, A, B)


if __name__ == '__main__':
    main()
