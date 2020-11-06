import time


class Node:
    def __init__(self, dataval):
        self.dataval=dataval
        self.nextval=None


class LinkedList:
    def __init__(self):
        self.headval = None # Head node in the linked list.

def printVals(t=Node()):
    print(t.dataval)
    if not(t.nextval is None):
        printVals(t.nextval)

def tailInsert(endnode=Node(), newnode=Node()):
     endnode.nextval = newnode
     
def headInsert(targetList = LinkedList(), newNode=Node()):
    newNode.nextval = targetList.headval
    targetList.headval = newNode


def getHead(llist=LinkedList()):
    print(llist.headval)


# def deleteList(head=Node):
#     if head is None:
#         print("done.")
#         return
#     else:
#         focus = head
#         del head
#         focus = focus.nextval
#         deleteList(focus)




valCount = (int)(input("This program is used to simulate a linked list data structure."
                 " How many values would you like to enter into the list? "))

myList = LinkedList()
focus = myList.headval
inputCount = 0

while inputCount < valCount:
    if myList.headval is None:
            newNode = Node(input("Enter Value #{}: ".format(inputCount+1)))
            myList.headval = newNode
            focus = myList.headval
            tailInsert(myList.headval, newNode)

    else:
            newNode = Node(input("Enter Value #{}: ".format(inputCount+1)))
            tailInsert(focus, newNode)
            focus = newNode

    inputCount += 1

printVals(myList.headval)

print("The head of the linked list is a node that contains the value {}.".format(myList.headval.dataval))
headInsert(myList, Node("1000"))
print("The head of the linked list is a node that contains the value {}.".format(myList.headval.dataval))

# deleteList(myList.headval)
# print("Values deleted.")
