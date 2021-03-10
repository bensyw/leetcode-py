class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        # In the end, we use start and end to index the string and find the substring
        length, longestPalStart, longestPalLength = len(s), 0, 1
        # Create N*N Dp table
        dp = [[None for _ in range(0, length)] for _ in range(0, length)]
        # Base case: A single char substring is pal
        for i in range(0, length):
            dp[i][i] = True
        # Working from the bottom right corner
        for start in reversed((range(0, length))):
            for end in range(start + 1, length):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end-1]:
                        dp[start][end] = True
                        if (longestPalLength < end - start + 1):
                            longestPalStart = start
                            longestPalLength = end - start + 1
        return s[longestPalStart:longestPalLength+longestPalStart]
