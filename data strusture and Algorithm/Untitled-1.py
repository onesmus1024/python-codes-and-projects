
class binarytree:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
    
def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val))
        # Traverse right
        inorder(root.right)

root = binarytree(10)
node1=binarytree(20)
node2=binarytree(30)
node3=binarytree(40)
root.left=node1
root.right = node2
node1.left=node3
inorder(root)