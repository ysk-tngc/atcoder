# -*- coding: utf-8 -*-
import math
import sys
input = sys.stdin.readline


def main():
    k = int(input())
    a, b = map(int, input().split())

    result = False
    for i in range(a, b + 1):
        if i % k == 0:
            result = True
            break

    if result:
        print('OK')
    else:
        print('NG')


if __name__ == '__main__':
    main()
