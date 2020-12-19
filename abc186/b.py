# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A = []

    a_min = 101
    for _ in range(H):
        ai = list(map(int, input().split()))
        a_min = min(a_min, min(ai))
        A.append(ai)

    result = 0
    for i in range(H):
        for j in range(W):
            result += A[i][j] - a_min

    print(result)


if __name__ == '__main__':
    main()
