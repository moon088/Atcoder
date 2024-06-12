#A
N = int(input())
P = list(map(int,input().split()))
S = list(input())

direct_box={1:"R",0:"L"}

def count_cmb(direct):
    sheet = [0]*(N+1)
    cmb = 1
    indirect = 1 if direct ==0 else 0
    
    for target in P:
        #index無理やり
        kikite=(target+direct)%N 
        if kikite == 0:
            kikite =N
        
        sakate=(target+indirect)%N
        if sakate ==0:
            sakate=N    
        #print(P[i],cmb,kikite,sakate)
        if sheet[sakate]==1: #置くところと逆が埋まっているとき
            if S[target-1] == "?": 
                cmb = cmb*2
            sheet[kikite] = 1
            continue
        else:   #置くところと逆がうまっていない
            if S[target-1] == direct_box[direct]: #きき手がdirectならOK  
                sheet[kikite] =1 
                continue
            elif S[target-1] == direct_box[indirect]: #利き手がindirectなら０通り
                return 0
            else: #利き手決まっていないならdirectと仮定する
                sheet[kikite]=1
                continue
    return cmb

if S[P[0]-1] =="L":
    result = count_cmb(0)
    print(result%998244353)
elif S[P[0]-1] == "R":
    result = count_cmb(1)
    print(result%998244353)
else:
    result = count_cmb(1)+count_cmb(0)
    print(result%998244353)
    #print(count_cmb(1))
