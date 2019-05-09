"""
Link: https://leetcode.com/problems/validate-binary-search-tree/
Category: Tree
Tags:
Solved by: Tarık Taha Uygun
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root, max_value = float('inf'), min_value = float('-inf')):
        # if root is empty, we accept as valid BST
        if not root:
            return True
        if not min_value < root.val < max_value:
            return False
        """
         We update the min_value and max_value in the following criterias in every recursive iteration:
         * left subtree:
            ** max_value must be root.val or max_value - which one is less
            ** min_value must be -inf
         * right subtree:
            ** max_value must be inf
            ** min_value must be root.val or min_value - which one is greater
         
        """
        return self.isValidBST(root.left, min(max_value, root.val), min_value) and \
               self.isValidBST(root.right, max_value, max(root.val, min_value))


"""
Test case: 58 / 75 
[10,5,15,null,null,6,20]
"""

node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_15.left = node_6
node_15.right = node_20

node_10 = TreeNode(10)
node_10.left = node_5
node_10.right = node_15

leet_code = Solution()
print(leet_code.isValidBST(node_10))
