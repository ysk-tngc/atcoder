# -*- coding: utf-8 -*-
import sys
from functools import reduce
from operator import add
input = sys.stdin.readline


def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    n_array = list(map(lambda x: int(x), n_str))
    
    n_array_sum = reduce(add, n_array)
    one_count = len(list(filter(lambda x: x % 3 == 1, n_array)))
    two_count = len(list(filter(lambda x: x % 3 == 2, n_array)))
    
    if n_array_sum % 3 == 0:
        print(0)
        return

    if n_array_sum % 3 == 1:
        if n_len == 1:
            print(-1)
            return

        if n_len == 2:
            if one_count > 0:
                print(1)
            else:
                print(-1)
            return

        if one_count > 0:
            print(1)
        else:
            if two_count > 1:
                print(2)
            else:
                print(-1)
        return
    
    if n_array_sum % 3 == 2:
        if n_len == 1:
            print(-1)
            return

        if n_len == 2:
            if two_count > 0:
                print(1)
            else:
                print(-1)
            return

        if two_count > 0:
            print(1)
        else:
            if one_count > 1:
                print(2)
            else:
                print(0)
        return


if __name__ == '__main__':
    main()
