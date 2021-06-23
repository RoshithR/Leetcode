# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Python program to print level
# order traversal using Queue

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the
# height of a binary tree
# def printLevelOrder(root):
#     # Base Case
#     if root is None:
#         return
#
#     # Create an empty queue
#     # for level order traversal
#     queue = []
#
#     # Enqueue Root and initialize height
#     queue.append(root)
#
#     while (len(queue) > 0):
#
#         # Print front of queue and
#         # remove it from queue
#         print(queue[0].data)
#         node = queue.pop(0)
#
#         # Enqueue left child
#         if node.left is not None:
#             queue.append(node.left)
#
#         # Enqueue right child
#         if node.right is not None:
#             queue.append(node.right)

from collections import deque



def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root, ])
    while queue:
        # start the current level
        levels.append([])
        # number of elements in the current level
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # fulfill the current level
            levels[level].append(node.data)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # go to next level
        level += 1

    return levels
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
# printLevelOrder(root)
levelOrder(root)