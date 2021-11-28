# --- Binary Trees --- #

# Binary Tree node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Initializing Binary Tree nodes and connections
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# --- Searching --- #

# Depth First search -- Stack System Last In / First Out (LIFO)
# n number of nodes  -> Time Complexity O(n) - Space Complexity O(n)


def depth_first(root):
    if root == None:
        return []
    stack = [root]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current)
        if (current.right):
            stack.append(current.right)
        if (current.left):
            stack.append(current.left)
    return result

#for x in depth_first(a): print (x.value, end =" ")

# Depth First search with recursion


def depth_first_r(root):
    if root == None:
        return []
    left_values = depth_first_r(root.left)
    right_values = depth_first_r(root.right)
    children = left_values + right_values
    children.insert(0, root)
    return children

#for x in depth_first_r(a): print (x.value, end =" ")

# Breadth First search -- Queue System First In / First Out (FIFO)
# n number of nodes  -> Time Complexity O(n) - Space Complexity O(n)


def breadth_first(root):
    if root == None:
        return []
    values = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current)
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)
    return values

#for x in breadth_first(a): print (x.value, end =" ")

# Solving Breadth First recursively doesnt make much sense since recursion uses stacks,
# while we are using a queue system. Therefore its hard to get the correct ordering


# --- Tree Includes --- #

# Breadth First
def breadth_first_target(root, target):
    if root == None:
        return False
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == target:
            return True
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)
    return False

# print(breadth_first_target(a,f))
# print(breadth_first_target(a,g))

# Recursive Depth First


def depth_first_r_target(root, target):
    if root == None:
        return False
    if root == target:
        return True
    return depth_first_r_target(root.left, target) or depth_first_r_target(root.right, target)

# print(depth_first_r_target(a,f))
# print(depth_first_r_target(a,g))

# --- Tree Sum --- #


def treeSum(root):
    if root == None:
        return 0
    sum = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        sum += current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum


a1 = Node(10)
b1 = Node(2)
c1 = Node(31)
d1 = Node(4)
e1 = Node(54)
f1 = Node(16)

a1.left = b1
a1.right = c1
b1.left = d1
b1.right = e1
c1.right = f1

# print(treeSum(a1))

# --- Tree Min --- #


def treeMin(root):
    if root == None:
        return float('inf')
    min = root.value
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value < min:
            min = current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return min

# print(treeMin(a1))


def treeMin_r(root):
    if root == None:
        return float('inf')
    leftMin = treeMin_r(root.left)
    rightMin = treeMin_r(root.right)
    return min(root.value, leftMin, rightMin)

# print(treeMin_r(a1))

# --- Max Root to Leaf Path Sum --- #


def maxPathSum(root):
    if root == None:
        return float('-inf')
    if root.left == None and root.right == None:
        return root.value
    max_child = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.value + max_child

# print(maxPathSum(a1))


# --- Invert Binary Tree --- #

def invertTree(root):
    if root == None:
        return root
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.right = left
    root.left = right
    return root


a2 = Node(1)
b2 = Node(2)
c2 = Node(3)
d2 = Node(4)
e2 = Node(5)
f2 = Node(6)

a2.left = b2
a2.right = c2
b2.left = d2
b2.right = e2
c2.right = f2

#for x in breadth_first(a2): print (x.value, end =" ")
# invertTree(a2)
# print("")
#for x in breadth_first(a2): print (x.value, end =" ")
