def max_gold(matrix):
    n = len(matrix)
    if n == 0:
        return 0

    dp = [[0] * len(row) for row in matrix]
    dp[0][0] = matrix[0][0]

    for i in range(1, n):
        for j in range(len(matrix[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
            elif j < len(dp[i - 1]):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + matrix[i][j]

    return max(dp[-1])


mountain = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8]
]

print("Максимальна кількість золота:", max_gold(mountain))
