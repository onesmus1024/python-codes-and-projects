
def create_stack():
    stack=[]
    return stack

def Isempty(stack):
    return len(stack) == 0

def pop(stack):
    if(Isempty(stack)):
        print("THE STACK IS EMPTY")
    else:
        print("REMOVING ",end='')
        print(stack.pop())
def push(stack,element):
    print("INSERTING ",end='')
    print(element)
    stack.append(element)
def printstack(stack):
    print(stack)

stack = create_stack()
pop(stack)
push(stack,20)
push(stack,30)
printstack(stack)
pop(stack)
printstack(stack)

