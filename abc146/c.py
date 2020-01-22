# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    a, b, x = map(int, input().split())
    x_max = 10 ** 18
    result = {}
    result, n = calc(a, b, x, 0, x_max, result)
    print(n)


def calc(a, b, x, x_min, x_max, result):
    n = int((x_max - x_min) / 2) + x_min
    # print(a, b, x, x_min, x_max, n, result)
    if n in result.keys():
        return result, n

    dn = len(str(n))
    if (x - b * dn) / a > n:
        result[n] = True
        return calc(a, b, x, n, x_max, result)
    else:
        result[n] = False
        return calc(a, b, x, x_min, n, result)


if __name__ == '__main__':
    main()
