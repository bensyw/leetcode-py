class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create DP table
        dp = [[0 for _ in range(0, n)] for _ in range(0, m)]
        for i in range(0, m):
            dp[i][0] = 1
        for j in range(0, n):
            dp[0][j] = 1
        # Solving subproblems
        for i in range(1, m):
            for j in range(1, n):
                # Either from the left tile or the top tile
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
