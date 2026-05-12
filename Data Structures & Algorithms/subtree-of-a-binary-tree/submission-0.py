# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self, p: Optional[TreeNode], q: Optional[TreeNode]):

        stack= [(p,q)]

        while stack:

            curr1, curr2 = stack.pop(0)

            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False

            stack.append((curr1.left, curr2.left))
            stack.append((curr1.right, curr2.right))

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = [root]

        while stack:
            
            curr = stack.pop()

            if self.same(curr, subRoot):
                return True

            if curr and curr.right:
                stack.append(curr.right)
            if curr and curr.left:
                stack.append(curr.left)


        return False








        