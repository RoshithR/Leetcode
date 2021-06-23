# Given the root of a binary tree, determine if it is a valid binary search tree(BST).



class new_node:
    def __init__(self, key):
        self.value = key
        self.left=None
        self.right=None

def validate_BST(root, l=None, r=None):
    if root==None:
        return True

    if l!=None and root.value<=l.value:
        return False

    if r!=None and root.value>=r.value:
        return False

    return validate_BST(root.left,l,root) and validate_BST(root.right,root,r)




if __name__=="__main__":
    root = new_node(3)
    root.left = new_node(1)
    root.left.left = new_node(0)
    root.left.right = new_node(2)
    root.right = new_node(5)
    root.right.left = new_node(4)
    root.right.right = new_node(3)
    print(validate_BST(root))




























