# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7

    all_case = pow(2, n, mod) - 1
    nCa = conbination(n, a, mod)
    nCb = conbination(n, b, mod)
    result = all_case - nCa - nCb
    while (result < 0):
        result = result + mod
    print(result)


def conbination(n, r, mod):
    a = 1
    b = 1
    for i in range(1, r + 1):
        # print(a, b, i)
        a = (a * (n - i + 1)) % mod
        b = (b * i) % mod
    b = pow(b, mod - 2, mod)

    return (a * b) % mod


if __name__ == '__main__':
    main()
