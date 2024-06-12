#A

wallet = list(map(int,input().split()))
N = int(input())
X= list(map(int,input().split()))
#1,5,10,50,100,500

    

def pay_gohyaku():
    i=0   
    while wallet[5] >0 and i<N:
       use_gohyaku = min((X[i]//500),wallet[5])
       wallet[5]-=use_gohyaku
       X[i] -= use_gohyaku*500
       i+=1    
    return
pay_gohyaku()
#print(X,wallet)



def pay_hyaku():
    i=0   
    while wallet[4] >0 and i<N:
       use_hyaku = min((X[i]//100),wallet[4])
       wallet[4]-=use_hyaku
       X[i] -= use_hyaku*100
       i+=1    
    return
pay_hyaku()
#print(X,wallet)

def pay_gojyuu():
    i=0   
    while wallet[3] >0 and i<N:
       use_gojyuu = min((X[i]//50),wallet[3])
       wallet[3]-=use_gojyuu
       X[i] -= use_gojyuu*50
       i+=1    
    return
pay_gojyuu()
#print(X,wallet)

def pay_jyuu():
    i=0   
    while wallet[2] >0 and i<N:
       use_jyuu = min((X[i]//10),wallet[2])
       wallet[2]-=use_jyuu
       X[i] -= use_jyuu*10
       i+=1    
    return
pay_jyuu()
#print(X,wallet)

def pay_go():
    i=0   
    while wallet[1] >0 and i<N:
       use_go = min((X[i]//5),wallet[1])
       wallet[1]-=use_go
       X[i] -= use_go*5
       i+=1    
    return
pay_go()
#print(X,wallet)

def pay_iti():
    i=0   
    while wallet[0] >0 and i<N:
       use_iti = min(X[i],wallet[0])
       wallet[0]-=use_iti
       X[i] -= use_iti
       i+=1    
    return
pay_iti()
#print(X,wallet)

def all_zeros(array):
    if all(element == 0 for element in array):
        print("Yes")
    else:
        print("No")

all_zeros(X)

