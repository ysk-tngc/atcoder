# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    result = 'NO'
    for i in range(1, B + 1):
        if A * i % B == C:
            result = 'YES'

    print(result)


if __name__ == '__main__':
    main()
