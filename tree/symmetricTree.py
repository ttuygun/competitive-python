"""
Link: https://leetcode.com/problems/symmetric-tree/
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


class Solution(object):
    def isMirror(self, leftNode: TreeNode, rightNode: TreeNode):
        # Traverse inner nodes until if it has found any of the node is None. If it will be happen, we recursively
        # stack the true values and finally return one true which means tree is mirror. This statement can be think
        # as our finish statement.
        if leftNode is None and rightNode is None:
            return True
        # This is our continue statement. If both of the right and left node is not equal to None we need to check:
        elif leftNode is not None and rightNode is not None:
            # 1. If both of the left and right node has a value.
            # 2. Recursively traverse with node's left value and node's right value.
            # 3. Recursively traverse with node's right value and node's left value.
            # e.g. If we are in node 2, we need to check left node 2's left value (3) and right node 2's right value (3)
            # is equal. However, we also need to check left node 2's right value (4) and right node'2's left value (4)
            return (leftNode.val == rightNode.val) and \
                   self.isMirror(leftNode.left, rightNode.right) and \
                   self.isMirror(leftNode.right, rightNode.left)
        # If one of the node has a value but the other one is None, we can say that tree is not mirror.
        # So, this is our not mirror finish statement.
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        # get root's head and turns to a recursive call
        return self.isMirror(root, root)


"""
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""

node_1 = TreeNode(1)
node_2_l = TreeNode(2)
node_2_r = TreeNode(2)
node_3_l = TreeNode(3)
node_3_r = TreeNode(3)
node_4_l = TreeNode(4)
node_4_r = TreeNode(4)

node_1.left = node_2_l
node_1.right = node_2_r
node_2_l.left = node_3_l
node_2_l.right = node_4_l
node_2_r.left = None
node_2_r.right = node_3_r

leet_code = Solution()
print(leet_code.isSymmetric(node_1))