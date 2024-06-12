#C
from bisect import bisect, bisect_left, insort, insort_left
N = int(input())
A=list(map(int,input().split()))

A.sort()
mod=10**8
sum=0
for i in range(N):
    sum+= A[i]*(N-1)
    idx = bisect_left(A,mod-A[i])
    cnt = min(N - i - 1, N - idx)
    sum-=cnt*mod
print(sum) 