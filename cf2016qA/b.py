# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    result = 0
    for i in range(N):
        j = a[i] - 1
        j_like = (a[a[i] - 1] - 1)
        if i < j and i == j_like:
            result += 1

    print(result)


if __name__ == '__main__':
    main()
