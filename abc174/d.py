# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    c = list(input())

    lead = 0
    tail = n - 1
    result = 0
    while(lead < tail):
        if c[lead] == 'R':
            lead += 1
            continue
        if c[tail] == 'W':
            tail -= 1
            continue

        c[lead] = 'R'
        c[tail] = 'W'
        result += 1
        lead += 1
        tail -= 1

    print(result)


if __name__ == '__main__':
    main()
