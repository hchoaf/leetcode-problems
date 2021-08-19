# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Find the maximum depth of a binary tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root != None else 0
    