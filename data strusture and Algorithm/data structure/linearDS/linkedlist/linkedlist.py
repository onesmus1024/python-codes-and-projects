class Node:
    def __init__(self,data) -> None:
        self.data =data;
        self.nextNode=None

    

node1 = Node(7)
node2 = Node(2)
node3 = Node(3)
node4=Node(10)
node5=Node(20)
node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4
node4.nextNode=node5

currentNode = node1
while True:
    print(currentNode.data,end='->')
    if currentNode.nextNode is None:
        print("None")
        break
    else:
        currentNode=currentNode.nextNode