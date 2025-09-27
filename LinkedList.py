class Node:
    def __init__(self):
        self.data = int()
        self.next = None

class LinkedList:
    head = Node()
    def __init__(self):
        self.head = None

    def insertNode(self, pos : int, data : int):
        new_node = Node()
        new_node.data = data
        if pos < 0:
            print("Position out of bound")
            exit()
        elif pos == 0:
            self.head.next = new_node
            new_node.next = None
        else:
            count = 0
            temp = Node()
            temp = self.head
            while temp != None and count < pos:
                temp = temp.next
                count += 1

            if temp == None:
                print("Position out of bound")
                return -1

            new_node.next = temp.next
            temp.next = new_node




