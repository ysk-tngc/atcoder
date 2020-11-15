# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    result = 2 * a + 100
    print(result - b)


if __name__ == '__main__':
    main()
