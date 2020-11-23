# -*- coding: utf-8 -*-
# 27:50 でギブアップ
import math
import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p_set = set(p)
    p_dict = dict()
    for i in p_set:
        r_sum = (i * (i + 1) / 2) / i
        p_dict[i] = r_sum

    r_prev = 0
    for i in range(K):
        r_prev += p_dict[p[i]]

    r_max = r_prev
    for i in range(1, N - K + 1):
        r_temp = r_prev + p_dict[p[i + K - 1]] - p_dict[p[i - 1]]

        if r_temp > r_max:
            r_max = r_temp

        r_prev = r_temp

    print(r_max)


if __name__ == '__main__':
    main()
