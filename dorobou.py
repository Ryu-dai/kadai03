W = int(input())
N = int(input())

p = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)] # 品物-> (価値, 重さ)
dp = [[0] * (W+1) for _ in range(N+1)] # 縦が品物の番号、横が現在の容量、dpの中身が最大の価値とする

for i in range(1, N+1):
    for j in range(1, W+1):

        if j-p[i][1] >= 0:
            dp[i][j] = max(dp[i-1][j],
                           dp[i-1][j-p[i][1]] + p[i][0])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])