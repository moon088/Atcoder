<<<<<<< HEAD
#B

N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    S,T=map(int,input().split())
    while A[i]>=S:
        A[i] -=S
        A[i+1]+=T
=======
#B

N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    S,T=map(int,input().split())
    while A[i]>=S:
        A[i] -=S
        A[i+1]+=T
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(A[N-1])