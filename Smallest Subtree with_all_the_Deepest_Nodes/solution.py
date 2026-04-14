'''
Definition for a binary tree node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return (0, None)

            left_depth, left_node = dfs(node.left) #йдемо вліво і вправа
            right_depth, right_node = dfs(node.right)

            if left_depth == right_depth:#однакової глибини - каррент вузол і є відповідь
                return left_depth + 1, node

            if left_depth > right_depth:#десь зліва
                return left_depth + 1, left_node
            return right_depth + 1, right_node#десь справа

        depth, answer = dfs(root)#повертаємо лише вузол!!?!?!?!?!?
        return answer
