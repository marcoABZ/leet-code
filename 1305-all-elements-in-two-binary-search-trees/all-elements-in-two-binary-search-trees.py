class Solution:
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        # 1. Turn the traversal into a generator
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        # 2. Merge two iterators instead of two lists
        def merge(g1, g2):
            # Pull the first values, defaulting to None if the tree is empty
            v1 = next(g1, None)
            v2 = next(g2, None)
            
            # While both generators have values, yield the smaller one
            while v1 is not None and v2 is not None:
                if v1 < v2:
                    yield v1
                    v1 = next(g1, None)
                else:
                    yield v2
                    v2 = next(g2, None)
            
            # 3. Flush whatever is left from the non-empty generator
            if v1 is not None:
                yield v1
                yield from g1
                
            if v2 is not None:
                yield v2
                yield from g2

        # Convert the final merged generator into a list to satisfy the return type
        return list(merge(inorder(root1), inorder(root2)))