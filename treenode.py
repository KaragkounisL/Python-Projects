# Custom Binary Tree Library -- Leonidas Karagkounis
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self):
        return str(self.val)

    # Initialize Tree from a list inserting values
    def TreeFromList(self, l):
        if len(l) == 0:
            return None
        root = TreeNode(l[0])
        queue = [root]
        i = 1
        while queue and i < len(l):
            node = queue.pop(0)
            if l[i] != None:
                node.left = TreeNode(l[i])
                queue.append(node.left)
            if l[i + 1] != None:
                node.right = TreeNode(l[i + 1])
                queue.append(node.right)
            i += 2
        return root

        # preorder traversal

    def TreePreorder(self, root):
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # print the tree in level order skipping the null nodes
    def TreePrint(self, root):
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node.val != None:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    # inorder traversal
    def TreeInorder(self, root):
        if root == None:
            return []
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    # postorder traversal
    def TreePostorder(self, root):
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    # level order traversal
    def TreeLevelorder(self, root):
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    # max depth of a tree
    def TreeMaxDepth(self, root):
        if root == None:
            return 0
        return max(self.TreeMaxDepth(root.left), self.TreeMaxDepth(root.right)) + 1

    # min depth of a tree
    def TreeMinDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return min(self.TreeMinDepth(root.left), self.TreeMinDepth(root.right)) + 1

    # check if the tree is balanced
    def TreeIsBalanced(self, root):
        if root == None:
            return True
        if abs(self.TreeMaxDepth(root.left) - self.TreeMaxDepth(root.right)) > 1:
            return False
        return self.TreeIsBalanced(root.left) and self.TreeIsBalanced(root.right)

    # check if the tree is complete
    def TreeIsComplete(self, root):
        if root == None:
            return True
        queue = [root]
        flag = False
        while queue:
            node = queue.pop(0)
            if node.left:
                if flag:
                    return False
                queue.append(node.left)
            else:
                flag = True
            if node.right:
                if flag:
                    return False
                queue.append(node.right)
            else:
                flag = True
        return True

    # check if the tree is symmetric
    def TreeIsSymmetric(self, root):
        if root == None:
            return True
        return self.TreeIsSymmetric(root.left, root.right)

    # check if the tree is symmetric left and right
    def TreeIsSymmetric(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.TreeIsSymmetric(left.left, right.right) and self.TreeIsSymmetric(left.right, right.left)

    # check if either of two trees are subtrees of each other
    def TreeIsSubtree(self, root1, root2):
        if root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            return self.TreeIsSubtree(root1.left, root2.left) and self.TreeIsSubtree(root1.right, root2.right)
        return self.TreeIsSubtree(root1.left, root2) or self.TreeIsSubtree(root1.right, root2)

    # max sum of subtrees
    def TreeMaxSum(self, root):
        if root == None:
            return 0
        return max(self.TreeMaxSum(root.left) + root.val, self.TreeMaxSum(root.right) + root.val)

    # min sum of subtrees
    def TreeMinSum(self, root):
        if root == None:
            return 0
        return min(self.TreeMinSum(root.left) + root.val, self.TreeMinSum(root.right) + root.val)

    # check if the tree is a binary search tree
    def TreeIsBST(self, root):
        if root == None:
            return True
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False
        return self.TreeIsBST(root.left) and self.TreeIsBST(root.right)

    # breadth first search
    def TreeBFS(self, root):
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    # depth first search
    def TreeDFS(self, root):
        if root == None:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # invert a binary tree
    def TreeInvert(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.TreeInvert(root.left)
        self.TreeInvert(root.right)
        return root
