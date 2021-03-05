from typing import List
from collections import defaultdict, deque


class Solution:
    # Usign BFS + Kahn's algorithm to topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list from the prerequisites
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
