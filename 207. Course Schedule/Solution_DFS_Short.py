from typing import List
from collections import defaultdict


class Solution:
    # A shorter version of DFS topological sort
    # Use defaultdict to construct adjacency list
    # Use any/all to traverse child nodes
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        # Visited status
        # -1 being visited
        # 1 visited
        # 0 not visited
        visited = [0 for _ in range(numCourses)]

        def dfs(node):
            # If visited or being visited
            if visited[node] in {1, -1}:
                return visited[node] == 1
            # Start traversing this node and its childen
            visited[node] = -1
            # any() return True if any entry is True
            # any(not xxx) return False if any entry is False
            if any(not dfs(neighbour) for neighbour in graph[node]):
                return False
            visited[node] = 1
            return True
        # all(): return True if all entries are True
        return all(dfs(node) for node in range(numCourses))
