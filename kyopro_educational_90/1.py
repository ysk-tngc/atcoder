# -*- coding: utf-8 -*-
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    left = -1
    right = L + 1
    while right - left > 1:
        mid = left + (right - left) / 2
        if solve(N, L, K, A, mid) == False:
            right = mid
        else:
            left = mid
    print(left)


# M以上で区切られるピースの数がK+1以上の場合は True を返す
# 左からM以上で区切られる箇所を探す。このとき残りの部分もM以上で区切られれば、カウントをインクリメント。
# 上記で見つけた点からM以上で区切られる箇所を探す。このとき残りの部分もM以上で区切られれば、カウントをインクリメント、を繰り返し、区切り点の数が K 個以上であれば True を返す
def solve(N, L, K, A, M):
    count = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= M and L - A[i] >= M:
            count += 1
            pre = A[i]
        # print(N, L, K, A, M, count, pre)

    return count >= K


if __name__ == '__main__':
    main()
