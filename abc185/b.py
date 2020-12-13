# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    N, M, T = map(int, input().split())
    a, b = [], []
    for _ in range(M):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    result = N
    last_t = 0
    for i in range(M):
        temp = result - (a[i] - last_t)
        if temp > 0:
            result = temp
        else:
            print('No')
            return

        temp = result + (b[i] - a[i])
        result = temp if temp < N else N
        last_t = b[i]

    temp = result - (T - last_t)
    result = temp if temp > 0 else 0
    print('Yes' if result > 0 else 'No')


if __name__ == '__main__':
    main()
