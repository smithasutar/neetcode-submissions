# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root, float("-inf"), float("inf"))]
        

        while stack:

            curr, mini, maxi = stack.pop()

            if mini >= curr.val:
                return False
            if maxi <= curr.val:
                return False

            if curr and curr.right:
                stack.append((curr.right, curr.val, maxi))
                        
            if curr and curr.left:
                stack.append((curr.left, mini, curr.val))

        return True





