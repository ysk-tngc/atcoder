# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    t = input()[0:n]

    x = -(-(n + 2) // 3)
    s_part = ""
    for _ in range(x):
        s_part += "110"

    contains = False
    for i in range(3*x - n + 1):
        if s_part[i:i+n] == t[0:n]:
            contains = True
            break

    if not contains:
        print(0)
        return

    if t == "1":
        print(10**10 * 2)
        return

    if t == "11":
        print(10**10)
        return

    zero_count = 0
    for i in range(n):
        if t[i] == '0':
            zero_count += 1

    last_is_zero = t[n - 1] == '0'
    result = 10**10 - zero_count + 1 if last_is_zero else 10**10 - zero_count
    print(result)


if __name__ == '__main__':
    main()
