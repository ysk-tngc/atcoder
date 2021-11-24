# -*- coding: utf-8 -*-
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    N = int(input())

    if N % 2 != 0:
        return

    for i in range(2**N):
        kakko_bin = format(i, "0{}b".format(N))
        left = 0
        right = 0
        for j in kakko_bin:
            if j == '0':
                left += 1
            else:
                right += 1
            if left < right:
                break
        if (left + right) == N and left == right:
            print(kakko_bin.replace('0', '(').replace('1', ')'))


if __name__ == '__main__':
    main()
