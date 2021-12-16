
class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.next = None


linkedlist1 = LinkedList()

linkedlist1.head=Node(20)

nodetwo=Node(30)
nodethree=Node(40)
nodefour=Node(50)

linkedlist1.head.next=nodetwo
nodetwo.next=nodethree
nodethree.next=nodefour

while linkedlist1.head !=None:
    print(linkedlist1.head.data,end='=>')
    linkedlist1.head=linkedlist1.head.next