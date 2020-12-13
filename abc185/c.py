# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    L = int(input())
    print(combination(L - 1, 11))


def combination(n, r):
    if (r * 2 > n):
        r = n - r
    dividend = 1
    divisor = 1
    for i in range(1, r + 1):
        dividend *= (n-i+1)
        divisor *= i
    return dividend // divisor


if __name__ == '__main__':
    main()
