<<<<<<< HEAD
#A 

N = int(input())
countx, county = 0,0
for i in range(N):
    X, Y = map(int, input().split())
    countx += X
    county += Y

if countx > county:
    print("Takahashi")
elif countx < county:
    print("Aoki")
else:
    print("Draw")





=======
#A 

N = int(input())
countx, county = 0,0
for i in range(N):
    X, Y = map(int, input().split())
    countx += X
    county += Y

if countx > county:
    print("Takahashi")
elif countx < county:
    print("Aoki")
else:
    print("Draw")





>>>>>>> 5a60e3f (Sync local Atcoder directory)
