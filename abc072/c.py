# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    max_a = max(a)
    sum_l = [0] * (max_a + 1)
    for ai in a:
        sum_l[ai] += 1

    if len(sum_l) < 3:
        print(sum(sum_l))
        return

    result = 0
    for i in range((max_a + 1) - (3 - 1)):
        temp = sum_l[i] + sum_l[i + 1] + sum_l[i + 2]
        if temp > result:
            result = temp

    print(result)


if __name__ == '__main__':
    main()
