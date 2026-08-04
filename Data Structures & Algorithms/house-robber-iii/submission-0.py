# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # I thought if we rob root we consider granchildren 
        # if we roob root then the coresponding tree has 4 grand children
        # thinking of root/root.left/root.right per sub tree
        # we need to decide if we can rob a root or skip by selecting the children 
        # at a root level we can only think of what if I robbed or 
        # what if I skipped
        # bottom up vesion to root 
        def dfs(root) -> tuple(int,int):
            if not root:
                return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            rob = root.val + left[1] + right[1]
            skip = max(left) + max(right)
            return (rob,skip)
        return max(dfs(root))


        