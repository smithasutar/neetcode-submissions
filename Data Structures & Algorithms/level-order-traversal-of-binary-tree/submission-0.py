# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        levels = [[]]
        stack = [root]
        lvl = 0
        
        while stack:
            lvl = []
            for i in range(len(stack)):
                curr = stack.pop(0)
                lvl.append(curr.val)

                if curr and curr.left:
                    stack.append(curr.left)
                if curr and curr.right:
                    stack.append(curr.right)
                
            levels.append(lvl)

        levels.pop(0)
        return levels


