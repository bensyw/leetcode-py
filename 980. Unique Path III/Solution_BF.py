from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Find the starting point
        def find_starting_point(grid):
            for index_y, row in enumerate(grid):
                for index_x, square in enumerate(row):
                    if square == 1:
                        starting_x, starting_y = index_x, index_y
                        return (starting_x, starting_y)
        (starting_x, starting_y) = find_starting_point(grid)
        # Find the total number of empty squares
        total_squares = sum(row.count(0) for row in grid) + 1

        # Define and call DFS
        # DFS function to find the number of path starting from the current node
        def dfs(grid, x, y, num_of_remaining_squares):
            if (x < 0 or x == len(grid[0]) or  # x out of bound
                y < 0 or y == len(grid) or  # y out of bound
                    grid[y][x] == -1):  # obstacle
                return 0
            # Reaches the end and no more remaining squares
            if (grid[y][x] == 2):
                # Note: this is different from if (a and b) return 1
                return int(num_of_remaining_squares == 0)
            # Set the current node as obstacle, since each node should be only traversed once
            grid[y][x] = -1
            # search 4 directions
            num_of_paths = dfs(grid, x + 1, y, num_of_remaining_squares-1) + \
                dfs(grid, x - 1, y, num_of_remaining_squares-1) + \
                dfs(grid, x, y + 1, num_of_remaining_squares-1) + \
                dfs(grid, x, y - 1, num_of_remaining_squares-1)
            # Set the current node as empty so that dfs in other call stacks can still traverse this node
            # Further practice Similar methods: LC 51 / LC 37
            # Further read: Python scope / Why Python functions modify lists and dictionaries
            grid[y][x] = 0
            return num_of_paths
        return dfs(grid, starting_x, starting_y, total_squares)
