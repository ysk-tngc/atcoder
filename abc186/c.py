# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    N = int(input())

    result = 0
    for i in range(1, N + 1):
        n_str = str(i)
        oct_n_str = oct(i)[2:]
        if '7' in n_str or '7' in oct_n_str:
            result += 1

    print(N - result)


if __name__ == '__main__':
    main()
