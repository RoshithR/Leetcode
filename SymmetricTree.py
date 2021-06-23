# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Iterative solution

class new_node:
    def __init__(self, key):
        self.value=key
        self.left=None
        self.right=None


# def is_Symmetric(root):
#      if root==None:
#          return True
#      stack = [[root.left, root.right]]
#      while len(stack)>0:
#          pair = stack.pop(0)
#          left,right = pair[0],pair[1]
#          if left==None and right==None:
#              continue
#          if left==None or right==None:
#              return False
#          if left.value == right.value:
#              stack.insert(0,[left.left,right.right])
#
#              stack.insert(0,[left.right,right.left])
#          else:
#              return False
#      return True


# Recursive solution
#
# def is_Symmetric(root):
#     if root==None:
#         return True
#     else:
#         return is_Mirror(root.left,root.right)
#
# def is_Mirror(left, right):
#     if left==None and right==None:
#         return True
#     if left==None or right==None:
#         return False
#     if left.value==right.value:
#         return is_Mirror(left.left, right.right) and is_Mirror(left.right, right.left)
#     else:
#         return False
#
#
#
#
# if __name__=="__main__":
#     root = new_node(1)
#     root.left = new_node(2)
#     root.left.left = new_node(3)
#     root.left.right = new_node(4)
#
#     root.right = new_node(2)
#     root.right.right = new_node(3)
#     root.right.left = new_node(4)
#     print(is_Symmetric(root))


