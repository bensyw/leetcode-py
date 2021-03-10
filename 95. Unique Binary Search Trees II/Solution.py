# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(list_of_nodes):
            if not list_of_nodes:
                return [None]
            result = []
            for index, value in enumerate(list_of_nodes):
                left_results, right_results = helper(
                    list_of_nodes[:index]), helper(list_of_nodes[index+1:])
                for left in left_results:
                    for right in right_results:
                        root, root.left, root.right = TreeNode(
                            value), left, right
                        result.append(root)
            return result
        list_of_nodes = [i for i in range(1, n+1)]
        return helper(list_of_nodes) if list_of_nodes else []
