from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Create DP table
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(0, n)] for _ in range(0, m)]
        # Instead of initialize the first row and column
        # We can start the state transition from (0,0)
        # Solve subproblems
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # Origin
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    # first row
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    # first column
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    # rest
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
