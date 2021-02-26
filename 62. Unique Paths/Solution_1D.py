class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use column DP table
        dp = [1 for _ in range(0, m)]
        # Add early termination
        if m == 1 or n == 1:
            return 1
        # Only needs to update range(1,m), since the first entry should always be 1
        for j in range(1, n):
            for i in range(1, m):
                dp[i] = dp[i] + dp[i-1]
        return dp[i]
