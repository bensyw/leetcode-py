class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Create DP table (column only)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1 for _ in range(0, m)]
        # Solve subproblems
        for j in range(0, n):
            for i in range(0, m):
                if obstacleGrid[i][j] == 1:
                    dp[i] = 0
                else:
                    # Origin
                    if i == 0 and j == 0:
                        dp[i] = 1
                    # first row
                    elif i == 0:
                        dp[i] = dp[i]
                    # first column
                    elif j == 0:
                        dp[i] = dp[i-1]
                    # rest
                    else:
                        dp[i] = dp[i-1] + dp[i]
        return dp[-1]
