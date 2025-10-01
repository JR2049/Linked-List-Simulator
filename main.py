class Node():

    def __init__(self, data):
        self.data = data
        self.pointer = None


class SLinkedList():

    def __init__(self):
        self.head = None

    def length(self):
        if self.head == None:
            return 0
        currentNode = self.head
        count = 1
        while currentNode.pointer != None:
            currentNode = currentNode.pointer
            count += 1
        return count

    def addNode(self, node):
        if self.length() == 0:
            self.head = node
        else:
            endNode = self.head
            while endNode.pointer != None:      # skip through the nodes to find the final node in the list
                endNode = endNode.pointer
            endNode.pointer = node              # set the final node's pointer to the newly-added node
        print(f"The node {node.data} has been added to the list.")

    def insertNode(self, node, idx):
        if self.length() == 0:
            self.head = node
        elif idx <= 0:
            oldHead = self.head
            self.head = node
            self.head.pointer = oldHead
        elif idx < self.length():
            currentNode = self.head             # start counting from the start of the list
            for i in range(idx - 1):
                currentNode = currentNode.pointer
            nextNode = currentNode.pointer
            currentNode.pointer = node
            node.pointer = nextNode
        elif idx >= self.length():
            endNode = self.head
            while endNode.pointer != None:      # skip through the nodes to find the final node in the list
                endNode = endNode.pointer
            endNode.pointer = node              # set the final node's pointer to the new node

    def deleteNode(self, node):
        if node == self.head:                       # delete the node at the head of the list
            nextNode = self.head.pointer
            self.head.pointer = None
            self.head = nextNode
            print(f"The node {node.data} has been deleted from the head of the list.")
            return
        currentNode = self.head
        prevNode = None
        while currentNode.pointer != None:
            nextNode = currentNode.pointer
            if currentNode == node:
                prevNode.pointer = nextNode
                currentNode.pointer = None
                print(f"The node {node.data} has been deleted.")
                return
            prevNode = currentNode
            currentNode = nextNode
        if currentNode == node:
            prevNode.pointer = None
            print(f"The node {node.data} has been deleted from the end of the list.")
            return
        print(f"The node {node.data} is not in the list.")

    def reverseList(self):
        currentNode = self.head
        prevNode = None
        while currentNode.pointer != None:
            nextNode = currentNode.pointer
            currentNode.pointer = prevNode
            prevNode = currentNode
            currentNode = nextNode
        currentNode.pointer = prevNode                          # set the end node's pointer to the previous node
        self.head = currentNode                                 # set the new head to the end node of the old list

    def swapNodes(self, ix1, ix2):
        if ix1 == ix2:
            print("The indices are the same. No swap necessary.")
            return
        length = self.length()
        if ix1 >= length or ix1 < 0:
            print("Index 1 out of bounds.")
            return
        if ix2 >= length or ix2 < 0:
            print("Index 2 out of bounds.")
            return
        if ix1 - ix2 == 1 or ix2 - ix1 == 1:                    # swap adjacent nodes
            if ix1 > ix2:
                ix = ix2
            else:
                ix = ix1
            currentNode1, currentNode2 = self.head, self.head.pointer
            prevNode, nextNode = None, currentNode2.pointer
            count = 0
            while count < ix:
                nextNode = currentNode2.pointer
                prevNode = currentNode1
                currentNode1 = currentNode2
                currentNode2 = nextNode
                count += 1
            if ix == 0:
                self.head = currentNode2
            else:
                prevNode.pointer = currentNode2
            currentNode1.pointer = currentNode2.pointer
            currentNode2.pointer = currentNode1
            print(f"Nodes {currentNode1.data} and {currentNode2.data} have been swapped.")
            return
        # Swap non-adjacent nodes
        currentNode1 = self.head
        prevNode1, nextNode1 = None, currentNode1.pointer
        count = 0
        while count < ix1:
            nextNode1 = currentNode1.pointer
            prevNode1 = currentNode1
            currentNode1 = nextNode1
            count += 1
        currentNode2 = self.head
        prevNode2, nextNode2 = None, currentNode2.pointer
        count = 0
        while count < ix2:
            nextNode2 = currentNode2.pointer
            prevNode2 = currentNode2
            currentNode2 = nextNode2
            count += 1
        nextNode1 = currentNode1.pointer
        nextNode2 = currentNode2.pointer
        if ix1 == 0:
            self.head = currentNode2
            currentNode2.pointer = nextNode1
            currentNode1.pointer = nextNode2
            prevNode2.pointer = currentNode1
        elif ix2 == 0:
            self.head = currentNode1
            currentNode1.pointer = nextNode2
            currentNode2.pointer = nextNode1
            prevNode1.pointer = currentNode2
        else:
            currentNode1.pointer = nextNode2
            currentNode2.pointer = nextNode1
            prevNode1.pointer = currentNode2
            prevNode2.pointer = currentNode1
        print(f"Nodes {currentNode1.data} and {currentNode2.data} have been swapped.")

    def printList(self):
        if self.head == None:
            print("The list is empty.")
            return
        output = ""
        currentNode = self.head
        while currentNode.pointer != None:
            output += currentNode.data + " -> "
            currentNode = currentNode.pointer
        output += currentNode.data
        print("---")
        print(output)
        print("---")

    def bubbleSort(self):
        swapped = True
        while swapped:
            swapped = False
            node1, node2 = self.head, self.head.pointer
            for i in range(self.length() - 1):
                if node1.data > node2.data:
                    self.swapNodes(i, i + 1)
                    swapped = True
                node1 = node2
                node2 = node2.pointer

    def selectionSort(self):
        length = self.length()
        for i in range(length):
            currentNode = self.head
            for k in range(i):
                currentNode = currentNode.pointer
            min = currentNode.data
            ixMin = i
            for j in range(i, length - i - 1):
                currentNode = currentNode.pointer
                if currentNode.data < min:
                    min = currentNode.data
                    ixMin = i + j + 1
                print(i+j)
            print(f"Min: {min}, {ixMin}")
            self.swapNodes(i, ixMin)


# -------------------------------------------------------------------------------------------
# TEST CODE


list = SLinkedList()

nodeA = Node("Alpha")
nodeB = Node("Bravo")
nodeC = Node("Charlie")
nodeD = Node("Delta")
nodeE = Node("Echo")
nodeF = Node("Foxtrot")


list.addNode(nodeA)
list.reverseList()
list.printList()
list.addNode(nodeB)
list.addNode(nodeC)
list.addNode(nodeD)
list.printList()
list.addNode(nodeE)
list.printList()
list.reverseList()
list.printList()
list.insertNode(nodeF, -1)
list.printList()
list.reverseList()
list.printList()

list.swapNodes(0, 5)
list.reverseList()
list.printList()

list.selectionSort()
list.printList()

