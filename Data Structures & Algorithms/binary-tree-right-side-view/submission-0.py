# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # this is also a level order problem 
        # you just need the last element to be seen in a particular level.
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            n = len(q) 
            ele = []
            for _ in range(n):
                
                cur = q.pop(0)
                ele.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                    
                if cur.right:
                    q.append(cur.right)
                    
            ans.append(ele)
        result = []
        print(ans)
        for a in ans:
            if a:
                result.append(a.pop())
        return result 

                

        
        