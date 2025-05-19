<<<<<<< HEAD
#D
from collections import defaultdict

MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for num in a:
    d[len(str(num))] += 1

res = 0
p10 = [1] * 11
for i in range(1, 11):
    p10[i] = p10[i - 1] * 10

for i in range(n):
    res += a[i] * i
    d[len(str(a[i]))] -= 1
    for j in range(1, 11):
        res += p10[j] * a[i] * d[j]

print(res % MOD)
=======
#D
from collections import defaultdict

MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for num in a:
    d[len(str(num))] += 1

res = 0
p10 = [1] * 11
for i in range(1, 11):
    p10[i] = p10[i - 1] * 10

for i in range(n):
    res += a[i] * i
    d[len(str(a[i]))] -= 1
    for j in range(1, 11):
        res += p10[j] * a[i] * d[j]

print(res % MOD)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
