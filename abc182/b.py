# -*- coding: utf-8 -*-
import sys
import numpy as np
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_max = max(a)
    gcd_values = np.empty(a_max + 1)
    for i in range(2, a_max + 1):
        values = list(map(lambda x: x % i == 0, a))
        gcd_values[i] = len(list(filter(lambda x: x, values)))

    print(gcd_values.argmax())

if __name__ == '__main__':
    main()
