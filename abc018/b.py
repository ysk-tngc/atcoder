# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    S = input()
    N = int(input())
    S = S[0:len(S) - 1]

    l = []
    r = []
    for _ in range(N):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)

    for i in range(N):
        s_left = S[0:l[i] - 1]
        s_middle = "".join(reversed(S[l[i] - 1: r[i]]))
        s_right = S[r[i]: len(S)]
        S = s_left + s_middle + s_right

    print(S)


if __name__ == '__main__':
    main()
