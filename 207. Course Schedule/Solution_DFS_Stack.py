from typing import List
from collections import defaultdict


class Solution:
    # Use a stack to track the current path (being visited)
    # Use a visited set to track the visited nodes
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list from the prerequisites
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # DFS cycle detection. Stack is the current path
        def dfs(node: int, stack: List[int]):

            if node in visited:
                if node in stack:
                    return True
                else:
                    return False

            visited.add(node)

            stack.append(node)
            for neighbour in graph[node]:
                if dfs(neighbour, stack):
                    return True
            stack.pop()

            return False

        visited = set()
        for node in range(numCourses):
            if dfs(node, []):
                return False
        return True
