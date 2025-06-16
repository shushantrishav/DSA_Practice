class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1]*n
        for i in range(1, m):
            curr = [1]*n
            for j in range(1, n):
                curr[j] = curr[j-1] + prev[j]
            prev = curr
        return prev[n-1]