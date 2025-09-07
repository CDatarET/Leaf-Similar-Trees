# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leaves(self, root, arr):
        if(root == None):
            return
        
        if(root.left == None and root.right == None):
            arr.append(root.val)
            return
        
        self.leaves(root.left, arr)
        self.leaves(root.right, arr)

    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        arr1 = []
        arr2 = []
        self.leaves(root1, arr1)
        self.leaves(root2, arr2)

        return(arr1 == arr2)
