'''
Definition for a binary tree node.
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left is None and node.right is None and node.val == targetSum:
                return True
            if node.left is not None:
                node.left.val += node.val
                queue.append(node.left)
            if node.right is not None:
                node.right.val += node.val
                queue.append(node.right)
        return False
