# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
        else:
            return 0