# AtCoderメモ

## bit操作色々
```python
#ライブラリ使ってやるベージョン
from itertools import product

for pro in product((0, 1), repeat=5):
    print(pro)
```
```python
#一からコーディング
"""
Aの部分集合の和がWに等しい場合の数
N=3,W=5,A=[1,2,3]
000~111までで、bitが1のところのindex iに対してA[i]を持ってくる。それの和
001->subset={A[0]}->sum=1
101->subset={A[0], A[2]}->sum=4
このうちわが５になるのは{A[1],A[2]}の一つなのでjudge((0,1,1))のみ1を返し、
他は0を返す。なのでans=1となる
"""

def judge(bit):
    S = 0
    for i in range(N):
        if bit & (1 << i):  
            S += A[i]

    if S == W:  
        return 1
    else:
        return 0

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for bit in range(1 << N):#range(2**N)と同値
    ans += judge(bit)
print(ans)
```


## UnionFind
[素集合データ構造](https://www.slideshare.net/chokudai/union-find-49066733)
[UnionFindについて](https://note.nkmk.me/python-union-find/)
[AtcoderによるUnionFind解説スライド](https://atcoder.jp/contests/atc001/tasks/unionfind_a)

* Union: 2つの集合を1つに併合する
* Find: ある要素がどの集合に属しているかを判定する


グループを作成したときにAとBが同一グループにあるか検索するとき、配列に要素を入れるだけではグループ要素数Nに対してθ(N)かかる。そこで木構造でUnionを行うことでFindするときは根にさかのぼり同一の根であるか判定すればよい。

ここでの問題点は最悪枝分かれのない一直線の木になってしまい、効率が悪い。そこでUnionのときに木の深さを保持して置き、深さの浅いほうを深いほうに結合することで対処する。

テンプレあり


## 経路探索
[Quita:結構わかりやすい](https://qiita.com/ageprocpp/items/cdf67e828e1b09316f6e)
### ベルマン・フォード法
負の重み付き最短経路導出。計算量はΘ(v^2+E)

```python    

def bellman_ford_max_score(N, edges):
    #初期化
    distance = [-INF] * (N + 1)
    distance[1] = 0  
    
    #リラクゼーション
    for _ in range(N - 1):
        for u, v, w in edges:
            if distance[u] != -INF and distance[u] + w > distance[v]:
                distance[v] = distance[u] + w
                
    #負の閉路の検出
    for _ in range(N - 1):
        updated = False
        for u, v, w in edges:
            if distance[u] != -INF and distance[u] + w > distance[v]:
                distance[v] = INF
                updated = True
        if not updated:
            break

    #出力
    if distance[N] == INF:
        print("inf")
    else:
        print(distance[N])
```


## 素数問題
### フェルマーの小定理

  a,pが互いに素ならa^(p-1)=1(mod p)
  言い換えればa^(-1)=a^(p-2)(mod p)

  これはaのmod pでの逆言を求めていることを意味する。
  とても大事。

```python
"""
解説:
V_X = X + X*10^N + ... + X*10^{(N-1)K}
    = X{10^(NX)-1}/(10^N-1) (\bacause 等比数列の和)
    
(bunshi) = X * pow(10 , N*X, mod) - 1    <-easy
(bunbo) -> mod p上での逆元bunbo^(-1)を計算する

ここで逆元の計算はフェルマーの小定理
    aとpが互いに素=>a^(p-1)=1  (mod p)
                <=>a^(-1)=a^(p-2)  (mod p)

これよりbunboの逆元はbunbo^(p-2)を計算すればいい

よって
V_N = X * {pow(10, N*X, mod) -1} / {10^N-1}^(mod-2)
で計算できる
"""
```

### エラトステネスの篩
あるx以下のすべての素数を発見したいとき、1~xの初期配列(True)を１~√xまで以下の操作を行う。あるtに対してtの倍数をすべてFalseにする。
やってることは、素数判定は√xまで調べればよく、調べている過程で合成数をすべてFalseにしていって残ったTrueが素数のリストになっているということ。



## セグメント木
ある演算(max,min,product,lcm,gcd,~,&,^)に関してある区間の演算を効率よく行える。
- 区間のえんざんがO(logn),値の1点更新がO(logn)で可能
logでノード更新できるのはかなり効率的。テンプレも用意してある。

一方でで値の更新は１点で(log)かかるため、１回の走査で複数区間の値の更新する際は非効率であり、それは遅延セグメントツリーを使う。セグ木、遅延セグ木ともにテンプレあり

### 遅延セグメントツリー
- 区間の演算がO(logn),<span style="color: yellow; ">値の区間更新が(logn)</span>で可能

ex.ABC340-E
