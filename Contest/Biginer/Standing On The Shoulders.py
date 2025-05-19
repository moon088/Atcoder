<<<<<<< HEAD
#C


N = int(input())

head = 0
height = 0
for i in range(N):
    A,B = map(int, input().split())
    head = max(head, B-A)
    height += A
=======
#C


N = int(input())

head = 0
height = 0
for i in range(N):
    A,B = map(int, input().split())
    head = max(head, B-A)
    height += A
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(height+head)