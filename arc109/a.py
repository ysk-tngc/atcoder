# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    a, b, x, y = map(int, input().split())

    if a == b:
        print(x)
        return

    if a > b:
        k_result = x
        k_result += (a - b - 1) * y
        r_result = x
        r_result += (a - b - 1) * 2 * x
        result = k_result if k_result < r_result else r_result
        print(result)
        return

    k_result = x
    k_result += (b - a) * y
    r_result = x
    r_result += (b - a) * 2 * x
    result = k_result if k_result < r_result else r_result
    print(result)


if __name__ == '__main__':
    main()
