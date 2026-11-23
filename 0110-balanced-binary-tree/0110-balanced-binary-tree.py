# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def rec_func(node : TreeNode) -> int: 
            #base case
            if node is None: 
                return 0

            #recursive case
            left_height = rec_func(node.left)
            right_height = rec_func(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1 

        if (rec_func(root) == -1):
            return False

        return True
        
        