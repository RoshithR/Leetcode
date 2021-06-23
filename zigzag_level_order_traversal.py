


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    ret = []
    level_list = deque()
    if root is None:
        return []
    # start with the level 0 with a delimiter
    node_queue = deque([root, None])
    is_order_left = True

    while len(node_queue) > 0:
        curr_node = node_queue.popleft()

        if curr_node:
            if is_order_left:
                level_list.append(curr_node.val)
            else:
                level_list.appendleft(curr_node.val)

            if curr_node.left:
                node_queue.append(curr_node.left)
            if curr_node.right:
                node_queue.append(curr_node.right)
        else:
            # we finish one level
            ret.append(level_list)
            # add a delimiter to mark the level
            if len(node_queue) > 0:
                node_queue.append(None)

            # prepare for the next level
            level_list = deque()
            is_order_left = not is_order_left

    return ret

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(33)
root.right.left = TreeNode(25)
root.right.right = TreeNode(40)
root.right.left.left = TreeNode(11)
root.right.right.left = TreeNode(34)
root.right.left.left.left = TreeNode(7)
root.right.left.left.right = TreeNode(12)
root.right.left.left.right.right = TreeNode(13)
root.right.right.left.right = TreeNode(36)
print(zigzagLevelOrder(root))