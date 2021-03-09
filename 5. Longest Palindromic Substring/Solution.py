class Solution:
    # Non-DP solution
    # Expand from each char to find the longest palindrome substring with thar char as the centre
    def longestPalindrome(self, s: str) -> str:
        # Early termination
        if s == s[::-1]:
            return s
        result = ""
        for i in range(len(s)):
            result = max(self.helper(s, i, i), self.helper(
                s, i, i + 1), result, key=len)
        return result

    # Return the longest substring can be expanded fron the substring
    def helper(self, substring: str, left: int, right: int):
        while left >= 0 and right < len(substring) and substring[left] == substring[right]:
            left -= 1
            right += 1
        return substring[left+1:right]
