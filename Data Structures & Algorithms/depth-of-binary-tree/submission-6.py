# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        lvl = 0

        while stack:
            
            for i in range(len(stack)):
                curr = stack.pop(0)

                if curr and curr.left:
                    stack.append(curr.left)
                if curr and curr.right:
                    stack.append(curr.right)
            
            
            lvl+=1


        return lvl



