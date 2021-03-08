from typing import List
from collections import defaultdict, deque


class Solution:
    # Usign BFS + Kahn's algorithm to topological sort
    # Intuition:
    # Step 1: Add the nodes with zero in-degree to the sorted array
    # Step 2: Reduce the in-degree based on the sorted nodes
    # Step 3: Add new nodes which have zero in-degree
    # Rinse and Repeat
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list from the prerequisites
        graph = defaultdict(list)
        # Create an list for keeping the degree
        degree = [0] * numCourses
        # Double check if the order of dependency is correct
        for y, x in prerequisites:
            graph[x].append(y)
            degree[y] += 1
        # Create a queue of nodes with zero degree
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        # Topological Sort
        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for neighbour in graph[node]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
        return topo_sort if len(topo_sort) == numCourses else []
