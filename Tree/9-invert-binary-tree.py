# link: https://leetcode.com/problems/invert-binary-tree/submissions/

# Invert (vertical flip) a given binary tree



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        
        self.invertTree(root.right)
        
        return root