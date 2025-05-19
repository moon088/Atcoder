<<<<<<< HEAD
#B
S = input()
T = input()

output=[]
count=0
for i in range(len(S)):
    for j in range(count,len(T)):
        #print(i,j,count,output)
        if S[i] == T[count]:
            output.append(j+1)
            count+=1
            break
        count += 1
            

for i in range(len(output)):
=======
#B
S = input()
T = input()

output=[]
count=0
for i in range(len(S)):
    for j in range(count,len(T)):
        #print(i,j,count,output)
        if S[i] == T[count]:
            output.append(j+1)
            count+=1
            break
        count += 1
            

for i in range(len(output)):
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    print(output[i],end=" ")