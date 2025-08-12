from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        res = []
        q = deque([root])

        while q:
            ans = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    ans.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if ans:
                res.append(ans)
        return res