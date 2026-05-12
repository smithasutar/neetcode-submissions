# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root, False)]
        heights = {}
        max_d = 0

        while stack:

            curr, visited = stack.pop()

            if not curr:
                continue

            if visited:
                left_h = heights.get(curr.left, 0)
                right_h = heights.get(curr.right, 0)

                heights[curr] = 1+max(left_h, right_h)

                max_d = max(max_d, left_h+right_h)

            else:
                stack.append((curr,True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))

        return max_d
