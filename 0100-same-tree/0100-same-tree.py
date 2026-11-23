# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def rec_fun(p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            
            if p is None or q is None: 
                return False 
            
            if p.val != q.val:
                return False 

            if not rec_fun(p.left, q.left):
                return False
            
            if not rec_fun(p.right, q.right):
                return False

            return True 

        return rec_fun(p, q)
        