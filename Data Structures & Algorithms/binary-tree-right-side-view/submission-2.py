# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right = []
        stack = [root]
        
        

        while stack:
            level = []

            for i in range(len(stack)):
                curr = stack.pop(0)
                if curr:
                    level.append(curr.val)

                if curr and curr.right:
                    stack.append(curr.right)
                if curr and curr.left:
                    stack.append(curr.left)
            if level:
                right.append(level[0])

        return right