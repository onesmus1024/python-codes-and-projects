class Node:
    def __init__(self,value):
        self.LeftNode=None 
        self.value=value
        self.RightNode=None
rootNode = Node(1)
rootNode.LeftNode=Node(2)
rootNode.RightNode=Node(3)
