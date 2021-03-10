class Solution:
    # Naive recursive method. Time Limit Exceeded
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 0
        # Break down G to F
        for i in range(1, n+1):
            # Break down F to the product of G
            result += self.numTrees(i-1) * self.numTrees(n-i)
        return result
