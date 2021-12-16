
class Queue:
    def __init__(self) -> None:
        self.queue=[]
        self.front=-1
        self.rear=-1

    def Isempty(self):
        if (len(self.queue)<1):
            return True
        else:
            return False
    def dequeue(self):
        if(self.Isempty()):
            print("the queue is empty")
        else:
            print("REMOVING")
            print(self.queue.pop(self.front))
    
    def enqueue(self,item):
        if(self.front == -1):
            print("ADDING")
            print(item)
            self.front+=1
            self.rear+=1
            self.queue.append(item)
        else:
            self.rear+=1
            self.queue.append(item)

    def display(self):
        print(self.queue)


q1 =   Queue()
q1.display()
q1.enqueue(20)
q1.enqueue(40)
q1.enqueue(40)
q1.enqueue(40)
q1.enqueue(40)
q1.enqueue(40)

q1.display()
q1.dequeue()
q1.display()
