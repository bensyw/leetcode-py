from typing import List


class Solution:
    # Upon seeing the note that A.length < 20, we should know that polynomial solution doesn't exist. The eventual time complexity must be exponential.
    def shortestSuperstring(self, words: List[str]) -> str:
        # Construct a weighted direct graph
        # The weight in [i][j] is the number of letters required to transform i to j
        num_of_words = len(words)
        adjacency_matrix = [[0] * num_of_words for _ in range(num_of_words)]
        for i in range(num_of_words):
            for j in range(num_of_words):
                # Iterate from the longgest suffix of i to the shortest suffix
                # Only needs to test the shorter length between i and j
                for k in range(min(len(words[i]), len(words[j])), -1, -1):
                    # The suffix of i is the same as the prefix of j
                    if words[i][-k:] == words[j][:k]:
                        adjacency_matrix[i][j] = k
                        break
        # The problem converts to a hamiltonian path problem
        # Find the shortest path that all nodes are traversed once
        # Time complexity O(2^n n^2)
        # 2^n to encode the visited words in binary string (One-hot)
        # n possible ending word
        # for each possible ending word, find the parent with the minimum cost (n parent)
        # Space complexity O(2^n n)

        # Initialize the DP table
        dp = [[''] * num_of_words for _ in range(1 << num_of_words)]
        # Outer loop: encoded binary
        for i in range(1 << num_of_words):
            # Inner loop: ending word
            for k in range(num_of_words):
                # If the ending word is not flagged as 1 in the encoded binary
                if not (i & (1 << k)):
                    continue
                # If only one word is used
                if i == 1 << k:
                    dp[i][k] = words[k]
                    continue
                # Subproblems: minimum cost to add the ending word j to the parent
                for j in range(num_of_words):
                    #
                    if j == k:
                        continue
                    if i & (1 << j):
                        # Previous state: remove ending word k from the current state
                        prev = i ^ (1 << k)
                        # If the previous state ends with j
                        s = dp[prev][j]
                        # The cost of transforming j to k
                        cost = adjacency_matrix[j][k]
                        # Construct the current state by add k to the previous state ending with j
                        s += words[k][cost:]
                        # Only update if the total length is smaller
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s

        # Find the superstring with the minimum length
        min_len = float('inf')
        result = ''
        for i in range(num_of_words):
            # (1 << num_of_words) - 1 means all words are used
            # s ends with i
            s = dp[(1 << num_of_words) - 1][i]
            if len(s) < min_len:
                min_len, result = len(s), s
        return result
