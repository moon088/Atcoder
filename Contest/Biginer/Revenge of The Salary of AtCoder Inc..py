N=int(input())
A=list(map(int,input().split()))
Mod=998244353

ni=pow(N,-1,Mod)

es=0
for i in range(N-1,-1,-1):
    e0=(ni*es+A[i])%Mod
    es+=e0
    es%=Mod

es*=ni
es%=Mod
print(es)