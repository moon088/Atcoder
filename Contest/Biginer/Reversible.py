<<<<<<< HEAD
N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
=======
N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(len(t))