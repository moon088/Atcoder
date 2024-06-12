#B


def last_digit_power(N, M, K):
    if M % 2 == 1:
        return pow(2, (N % (M - 1)) * (M - 2), 10)
    else:
        return pow(2, (N % (M - 1)) * (M // 2 - 1), 10)

# テストケース数
T = int(input())

# T 個のテストケースについて答えを求める
for _ in range(T):
    N, M, K = map(int, input().split())
    print(last_digit_power(N, M, K))
