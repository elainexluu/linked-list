# Date: April 29, 2022
# more technical version of coding linked list in Python


class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

# create linked list class
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # create insert node function
    def insertNode(self, value):
        # create a node from value because it will be empty
        node = Node(value)
        # check if list is empty (tail node)
        # if empty->make current node the head node, if not empty->keep traversing
        
        if self.head == None:
            self.head = node
            return

        curr = self.head # store head node in new variable
        while True:
            if curr.nextNode == None: # if next node on list is empty, insert node
                curr.nextNode = node
                break
            else:
                curr = curr.nextNode # keep traversing if list not empty

    # display node function
    def printNode(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode

        

# testing

test = LinkedList()
test.insertNode("2")
test.insertNode("8")
test.insertNode("4")
test.printNode()