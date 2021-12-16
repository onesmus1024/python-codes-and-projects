class LinkedListNode:
    def __init__(self,data,nextNode=None) -> None:
        self.data=data
        self.nextNode = nextNode



class LinkedList:
    def __init__(self,head=None) -> None:
        self.head=head
    def insert(self,data):
        node=LinkedListNode(data)
        
        if self.head is None:
            self.head=node
            return
        currentNode=self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode=currentNode.nextNode

    def TraverseLinkedList(self):
        if self.head is None:
            print("there is no node in the linked list")
        currentNode=self.head
        while True:
            print(currentNode.data,end='->')
            if currentNode.nextNode is None:
                print("no other none")
                break
            currentNode = currentNode.nextNode


if __name__ == "__main__":
    linklist1 = LinkedList()
    linklist1.insert(20)
    linklist1.insert(30)
    linklist1.TraverseLinkedList()
