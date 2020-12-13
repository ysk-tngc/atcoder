# -*- coding: utf-8 -*-
from functools import reduce
import math
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A = sorted(A)

    white_count_list = []
    index = 1
    for j in range(M):
        count = A[j] - index
        if count != 0:
            white_count_list.append(count)
        index = A[j] + 1

    count = N - index + 1
    if count != 0:
        white_count_list.append(count)

    if len(white_count_list) == 0:
        print(0)
        return

    min_count = min(white_count_list)
    result = 0
    for i in white_count_list:
        result += -(-i // min_count)

    print(result)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


if __name__ == '__main__':
    main()
