# Leetcode 337_House Robber III

# importing my custom library for binary trees
from treenode import TreeNode

# initializing the root node and the list of nodes from given list
tree = TreeNode()
tree.__init__()
root = tree.TreeFromList([3, 2, 3, None, 3, None, 1])

# Implementing the solution


class Solution:
    def rob(self, root) -> int:
        return max(self.rob_helper(root))

    def rob_helper(self, root):
        if not root:
            return (0, 0)
        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)
        return (max(left[0], left[1]) + max(right[0], right[1]), left[0] + right[0] + root.val)


print(Solution().rob(root))
