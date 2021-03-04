from typing import List


class Solution:
    # DFS Topological Sort
    # The question is equivalent to detecting cycles in a directed graph
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list from the prerequisites
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        # Store the visited/visiting status of each node
        # -1 visited, 1 being visited, 0 not visited
        visited = [0 for _ in range(numCourses)]
        # Traverse each node
        for node in range(numCourses):
            if not self.dfs(graph, visited, node):
                return False
        return True

    # Explaination of the status
    # Being visited: The current path of DFS
    # Visited: This node and and the path from this node to leaves have been traversed before
    # Not visited: Self-explainary
    def dfs(self, graph, visited, node):
        # If this node is being visited, a cycle is found
        if visited[node] == -1:
            return False
        # If this node is visited before, no need to traverse it again
        if visited[node] == 1:
            return True
        # Mark this node as being visited:
        visited[node] = -1
        # Visit all neighbours
        for neighbour in graph[node]:
            if not self.dfs(graph, visited, neighbour):
                return False
        # After all neighbours are visited, mark the current node as visited
        visited[node] = 1
        return True
