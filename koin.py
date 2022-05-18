# 無限だけど役割的にはリストの要素の中の空の数
INF = float('inf')

#入力を受け付ける
n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))

#inf がn+1個あるリストをm+1個生成
dp = [[INF] * (n+1) for _ in range(m+1)]

#表の最初は０
dp[0][0] = 0


for i in range(1, m+1):
    for j in range(n+1):

        #新しいコインを使えるとき
        if j-coins[i] >= 0:
            #最小を選ぶ
            dp[i][j] = min(dp[i-1][j-coins[i]] + 1,
                           dp[i][j-coins[i]] + 1,
                           dp[i-1][j])

        #新しいコインを使えないとき
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m][n])