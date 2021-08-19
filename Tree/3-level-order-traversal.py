# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Traverse a binary tree in level-order 

# I used BFS using queue



from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([])
        
        q.appendleft([root])
        
        while(q):
            current = q.pop()
            temp = []
            temp_ans = []
            for node in current:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                temp_ans.append(node.val)
            if temp:
                q.appendleft(temp)
            if temp_ans:
                ans.append(temp_ans)
        return ans
            
        
        