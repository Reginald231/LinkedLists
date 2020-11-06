class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None  # Head node in the linked list.


def printVals(t=Node()):
    print(t.dataval)
    if not (t.nextval is None):
        printVals(t.nextval)


def tail_Insert(endnode=Node(), newnode=Node()):
    endnode.nextval = newnode


def head_Insert(targetList=LinkedList(), newNode=Node()):
    newNode.nextval = targetList.headval
    targetList.headval = newNode


def get_Head(llist=LinkedList()):
    print(llist.headval)


val_Count = (int)(input("This program is used to simulate a linked list data structure."
                        " How many values would you like to enter into the list? "))

myList = LinkedList()
focus = myList.headval
inputCount = 0

while inputCount < val_Count:
    if myList.headval is None:
        newNode = Node(input("Enter Value #{}: ".format(inputCount + 1)))
        myList.headval = newNode
        focus = myList.headval
        tail_Insert(myList.headval, newNode)

    else:
        newNode = Node(input("Enter Value #{}: ".format(inputCount + 1)))
        tail_Insert(focus, newNode)
        focus = newNode

    inputCount += 1

printVals(myList.headval)

print("The head of the linked list is a node that contains the value {}.".format(myList.headval.dataval))
head_Insert(myList, Node("1000"))
print("The head of the linked list is a node that contains the value {}.".format(myList.headval.dataval))
