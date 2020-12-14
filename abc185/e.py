# -*- coding: utf-8 -*-
from functools import reduce
import math
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    INF = 1001001001
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
            if i > 0 and j > 0:
                cost = 0
                if (A[i - 1] != B[j - 1]):
                    cost = 1
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + cost)

    print(dp[N][M])


if __name__ == '__main__':
    main()
