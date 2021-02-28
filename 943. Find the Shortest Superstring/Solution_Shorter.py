from typing import List


class Solution:
    # Use more factory functions to shorten the code
    # Worse performance
    def shortestSuperstring(self, words: List[str]) -> str:
        # Construct a weighted direct graph
        num_of_words = len(words)
        adjacency_matrix = [[0] * num_of_words for _ in range(num_of_words)]
        for i in range(num_of_words):
            for j in range(num_of_words):
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    # if j starts with the suffix of i
                    if words[j].startswith(words[i][-k:]):
                        adjacency_matrix[i][j] = k
                        break

        # Initialize the DP table
        dp = [[None] * num_of_words for _ in range(1 << num_of_words)]
        for i in range(1 << num_of_words):
            # only pick the ending words that's in the encoded binary i
            for k in filter(lambda x: (1 << x) & i, range(num_of_words)):
                # Previous state without ending k
                prev = i ^ (1 << k)
                dp[i][k] = min(
                    # Add k to the previous state with different ending j
                    [dp[prev][j] + words[k][adjacency_matrix[j][k]:]
                        for j in filter(lambda x: (1 << x) & prev, range(num_of_words))],
                    key=len,
                    default=words[k]
                )
        # Find the non-null last state, with the minimum length
        return min(filter(None, dp[-1]), key=len)
