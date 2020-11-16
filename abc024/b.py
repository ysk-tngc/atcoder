# -*- coding: utf-8 -*-
import sys
from functools import reduce
from operator import add
input = sys.stdin.readline


def main():
    n, t = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    result = t
    for i in range(1, n):
        if a[i - 1] + t > a[i]:
            result += a[i] - a[i - 1]
        else:
            result += t

    print(result)


if __name__ == '__main__':
    main()
