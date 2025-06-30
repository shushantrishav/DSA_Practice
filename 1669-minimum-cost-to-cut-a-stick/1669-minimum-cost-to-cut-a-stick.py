class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):  # interval length
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + cuts[j] - cuts[i]
                    )

        return dp[0][m - 1]