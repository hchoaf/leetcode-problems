# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

# Find the lowest common ancestor of two nodes in a binary search tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val or (root.val < q.val and p.val < root.val) or (root.val < p.val and q.val < root.val):
            return root
        else:
            if root.val < q.val and root.val < p.val:
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.val > q.val and root.val > p.val:
                return self.lowestCommonAncestor(root.left, p, q)
        
        
        
        