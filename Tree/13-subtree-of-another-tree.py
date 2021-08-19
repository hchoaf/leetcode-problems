# link: https://leetcode.com/problems/subtree-of-another-tree/

# check if tree has a subtree in it



class Solution:
    def isMatch(self, root, subRoot):
        if not (root and subRoot):
            return root is subRoot
        
        if root.val == subRoot.val:
            return self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)
        
        return False
        
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        if not root:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)