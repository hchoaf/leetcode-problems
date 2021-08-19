# link: https://leetcode.com/problems/validate-binary-search-tree/

# Check if given tree is a binary serach tree



class Solution:
    def in_order_traverse(self, nums, root:Optional[TreeNode]):
        if root is None:
            return
        self.in_order_traverse(nums, root.left)
        nums.append(root.val)
        self.in_order_traverse(nums, root.right)
        
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        self.in_order_traverse(nums, root)
        print(nums)
        
        return True if nums == sorted(nums) and len(nums) == len(set(nums)) else False