# https://atcoder.jp/contests/abc162/submissions/11860785
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    s = input()

    ans = s.count('R') * s.count('G') * s.count('B')
    # print(ans)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            k = (j - i) + j
            if k >= n:
                # print(i, j, k)
                break

            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
