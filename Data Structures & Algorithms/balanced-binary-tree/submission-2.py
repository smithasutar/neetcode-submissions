# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, False)]
        heights = {}

        while stack:

            curr, visited = stack.pop()

            if not curr:
                continue

            if visited:
                left_h = heights.get(curr.left, 0)
                right_h = heights.get(curr.right, 0)

                balance = abs(left_h-right_h)

                if balance > 1:
                    return False

                heights[curr] = 1+max(left_h, right_h)

            else:
                stack.append((curr, True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))

        return True

