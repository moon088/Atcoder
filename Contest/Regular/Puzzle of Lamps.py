<<<<<<< HEAD
#B

N = int(input())
S = list(map(int,input()))

status = [0]*N
out=[]
def make_on(index ,count):
    i=0
    while i<=index:
        status[i]=1        
        i+=1
        count+=1
        out.append("A")
    return count
        
def make_off(index,count):
    i=0
    while i<=index:
        status[i]=0
        i+=1
        count+=1
        out.append("B")
    return count

flag = 0
count=0
for i in range(N-1,-1,-1):
    if flag==0:#全部左0で右1を探す
        if S[i]==0:
            continue
        else:
            count = make_on(i,count)
            flag=1
            continue
    else:#全部左1で右０を探す
        if S[i]==1:
            continue
        else:
            count=make_off(i,count)
            flag = 0
            continue
print(count)
for i in range(len(out)):
    print(out[i],end="")


=======
#B

N = int(input())
S = list(map(int,input()))

status = [0]*N
out=[]
def make_on(index ,count):
    i=0
    while i<=index:
        status[i]=1        
        i+=1
        count+=1
        out.append("A")
    return count
        
def make_off(index,count):
    i=0
    while i<=index:
        status[i]=0
        i+=1
        count+=1
        out.append("B")
    return count

flag = 0
count=0
for i in range(N-1,-1,-1):
    if flag==0:#全部左0で右1を探す
        if S[i]==0:
            continue
        else:
            count = make_on(i,count)
            flag=1
            continue
    else:#全部左1で右０を探す
        if S[i]==1:
            continue
        else:
            count=make_off(i,count)
            flag = 0
            continue
print(count)
for i in range(len(out)):
    print(out[i],end="")


>>>>>>> 5a60e3f (Sync local Atcoder directory)
