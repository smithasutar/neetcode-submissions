class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            top = stack[-1]

            # still building left subtree
            if top.val != inorder[in_idx]:
                top.left = node
                stack.append(node)
            else:
                # unwind stack until we find where to attach right child
                while stack and stack[-1].val == inorder[in_idx]:
                    top = stack.pop()
                    in_idx += 1

                top.right = node
                stack.append(node)

        return root
