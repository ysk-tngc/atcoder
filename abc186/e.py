# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    T = int(input())
    N, S, K = [], [], []
    for _ in range(T):
        n, s, k = map(int, input().split())
        N.append(n)
        S.append(s)
        K.append(k)

    print(T, N, S, K)

    print()


def take_one(N, S, K):
    if N - S == K:
        return 1

    if N % 2 == 0:
        print()
    else:
        print()


if __name__ == '__main__':
    main()
