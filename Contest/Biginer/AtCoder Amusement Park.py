<<<<<<< HEAD
#B
N,K = map(int,input().split())
A=list(map(int,input().split()))
count=0
group =0
kuuseki = K
while group<N:
    if kuuseki<A[group]:
        count+=1
        kuuseki=K
    else:
        kuuseki -=A[group]
        group +=1
        
if kuuseki ==K:
    print(count)
else:
    print(count+1)
=======
#B
N,K = map(int,input().split())
A=list(map(int,input().split()))
count=0
group =0
kuuseki = K
while group<N:
    if kuuseki<A[group]:
        count+=1
        kuuseki=K
    else:
        kuuseki -=A[group]
        group +=1
        
if kuuseki ==K:
    print(count)
else:
    print(count+1)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
