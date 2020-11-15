# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc182/editorial/291
import sys
from functools import reduce
from operator import add
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_cum = []
    temp_cum = 0
    a_max = []
    temp_max = 0
    for i in range(n):
        temp_cum = temp_cum + a[i]
        a_cum.append(temp_cum)
        temp_max = temp_max if temp_max > temp_cum else temp_cum
        a_max.append(temp_max)

    result = 0
    x = 0
    for i in range(n):
        result = max(result, x + a_max[i])
        x = x + a_cum[i]

    print(result)


if __name__ == '__main__':
    main()
