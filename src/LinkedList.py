class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Prints all nodes after this one in the linked list
    def print(self, line_num):
        arr = []
        curr = self
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        print("Line {}: {}".format(line_num, arr))

class DoubleNode:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    # Prints all of the nodes in the linked list
    # that this node is in starting from the beginning
    def print(self, line_num):
        arr = []
        curr = self
        while curr.prev != None:
            curr = curr.prev
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        print("Line {}: {}".format(line_num, arr))
