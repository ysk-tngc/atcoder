# -*- coding: utf-8 -*-
from math import gcd
import sys
input = sys.stdin.readline


def main():
    n = int(input())

    a = []
    for i in range(2, n + 1):
        a.append(i)

    ans = a[0]
    for i in range(n - 1):
        ans = ans * a[i] // gcd(ans, a[i])
    print(ans + 1)


if __name__ == '__main__':
    main()
