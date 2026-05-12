# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, root.val)]
        good = 0

        while stack:
            curr, max_so_far = stack.pop()

            if curr.val >= max_so_far:
                good+=1

            new_max = max(curr.val, max_so_far)
            
            if curr and curr.right:
                stack.append((curr.right, new_max))

            if curr and curr.left:
                stack.append((curr.left, new_max))

        return good














