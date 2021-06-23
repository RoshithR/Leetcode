
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

# Python Program to print zigzag traversal
# of binary tree
#
# # Binary tree node
# class Node:
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
#
#
# # function to print zigzag traversal of
# # binary tree
# def zizagtraversal(root):
#     # Base Case
#     if root is None:
#         return
#
#     # Create two stacks to store current
#     # and next level
#     currentLevel = []
#     nextLevel = []
#
#     # if ltr is true push nodes from
#     # left to right otherwise from
#     # right to left
#     ltr = True
#
#     # append root to currentlevel stack
#     currentLevel.append(root)
#
#     # Check if stack is empty
#     while len(currentLevel) > 0:
#         # pop from stack
#         temp = currentLevel.pop(-1)
#         # print the data
#         print(temp.data, " ", end="")
#
#         if ltr:
#             # if ltr is true push left
#             # before right
#             if temp.left:
#                 nextLevel.append(temp.left)
#             if temp.right:
#                 nextLevel.append(temp.right)
#         else:
#             # else push right before left
#             if temp.right:
#                 nextLevel.append(temp.right)
#             if temp.left:
#                 nextLevel.append(temp.left)
#
#         if len(currentLevel) == 0:
#             # reverse ltr to push node in
#             # opposite order
#             ltr = not ltr
#             # swapping of stacks
#             currentLevel, nextLevel = nextLevel, currentLevel
#
#
# # Driver program to check above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(7)
# root.left.right = Node(6)
# root.right.left = Node(5)
# root.right.right = Node(4)
# print("Zigzag Order traversal of binary tree is")
# zizagtraversal(root)


class Node:
    def __init__(self, val):
        self.value=val
        self.left = self.right = None

def zigzag_traversal(root):
    #     if root is None:
    #         return
    #
    #     # Create two stacks to store current
    #     # and next level
    #     currentLevel = []
    #     nextLevel = []
    #
    #     # if ltr is true push nodes from
    #     # left to right otherwise from
    #     # right to left
    #     ltr = True
    #
    #     # append root to currentlevel stack
    #     currentLevel.append(root)
    #
    #     # Check if stack is empty
    #     while len(currentLevel) > 0:
    #         # pop from stack
    #         temp = currentLevel.pop(-1)
    #         # print the data
    #         print(temp.data, " ", end="")
    #
    #         if ltr:
    #             # if ltr is true push left
    #             # before right
    #             if temp.left:
    #                 nextLevel.append(temp.left)
    #             if temp.right:
    #                 nextLevel.append(temp.right)
    #         else:
    #             # else push right before left
    #             if temp.right:
    #                 nextLevel.append(temp.right)
    #             if temp.left:
    #                 nextLevel.append(temp.left)
    #
    #         if len(currentLevel) == 0:
    #             # reverse ltr to push node in
    #             # opposite order
    #             ltr = not ltr
    #             # swapping of stacks
    #             currentLevel, nextLevel = nextLevel, currentLevel
    if root==None:
        return

    current_level, next_level = [],[]
    ltr = True
    current_level.append(root)

    while len(current_level)>0:
        s = current_level.pop(-1)
        print(s.value)
        if ltr:
            if s.left:
                next_level.append(s.left)
            if s.right:
                next_level.append(s.right)
        else:
            if s.right:
                next_level.append(s.right)
            if s.left:
                next_level.append(s.left)

        if len(current_level)==0:
            current_level, next_level = next_level, current_level
            ltr = not ltr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzag_traversal(root)