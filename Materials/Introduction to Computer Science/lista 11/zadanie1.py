import sys


class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def insert_item(root, value):       # funckja pomocnicza
    if root is None:
        return TreeItem(value)
    if root.val > value:
        root.left = insert_item(root.left, value)
    elif root.val < value:
        root.right = insert_item(root.right, value)
    return root


# zadanie 2
def count_items(t):     
    if t is None:
        return 0
    return 1 + count_items(t.left) + count_items(t.right)


 # zadanie 3
def height(t):      
    if t is None:
        return 0
    leftAns = height(t.left)
    rightAns = height(t.right)
    return max(leftAns, rightAns) + 1

# zadanie 4
def write(t):        
    if t:
        write(t.left)
        if t.val > 0:
            print(t.val, end=' ')
        write(t.right)

# zadanie 5
def isBST(root, mini, maxi):        
    if root is None:
        return True
    if root.val <= mini:
        return False
    if root.val >= maxi:
        return False
    return isBST(root.right, root.val, maxi) and isBST(root.left, mini, root.val)


# zadanie 6
def combine(root, root2):       
    while root.right:
        root = root.right
    root.right = root2


# zadanie 7
def insert_iter(root, value): 
    curr = root
    parent = None
    while curr:
        parent = curr
        if value <= curr.val:
            curr = curr.left
        else:
            curr = curr.right

    if value < parent.val:
        parent.left = TreeItem(value)
    elif value > parent.val:
        parent.right = TreeItem(value)

    return root