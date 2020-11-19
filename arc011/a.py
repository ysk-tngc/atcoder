# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    m, n, N = map(int, input().split())

    remain = 0
    result = N
    while(N > 0):
        N = N + remain
        remain = (N) % m
        new = (N // m) * n
        result += new
        N = new

    print(result)


if __name__ == '__main__':
    main()
