class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        pv = p.val
        qv = q.val

        if pv == qv:
            # Vacuously true
            left = self.dfs(p.left, q.left)
            right = self.dfs(p.right, q.right)

            return left and right
        else:
            return False

    def dfs(self, p, q):
        return self.isSameTree(p, q)
