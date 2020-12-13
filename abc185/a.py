# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    a1, a2, a3, a4 = map(int, input().split())
    result = min(a1, min(a2, min(a3, a4)))
    print(result)


if __name__ == '__main__':
    main()
