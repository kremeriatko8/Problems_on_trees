'''
Definition for a binary tree node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root):
        if root.left is None and root.right is None:
            return root.val == 1#якщо листок то просто рівняємо з 1

        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)#рекурсіяяя

        if root.val == 2:#означає ор
            return left_result or right_result

        if root.val == 3:#означає енд
            return left_result and right_result
