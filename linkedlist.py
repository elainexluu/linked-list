# Date: April 4, 2022
# simple version of coding linked list in Python

# create a node class
class node:
    # create constructor
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

# create nodes
newNode = node("3")
node2 = node("4")
node3 = node("5")

newNode.nextNode = node2 # connect newnode to node2
node2.nextNode = node3 # connect node2 to node 3

# assign head node to new variable
currNode = newNode

# traverse through the linked list
while True:

    # check to see if current node is not tail node
    # if it is tail node, break loop, else keep traversing
    if currNode == None:
        break
    else:
        print(currNode.data)
        currNode = currNode.nextNode
        

    
