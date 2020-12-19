# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)
    result = 0
    for i in range(N):
        result -= (N - 1 - i) * A[i]
        result += i * A[i]

    print(result)


if __name__ == '__main__':
    main()
