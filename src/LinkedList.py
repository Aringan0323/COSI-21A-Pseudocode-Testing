class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


    def print(self):
        arr = []
        curr = self
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        print(arr)

class DoubleNode:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


    def print(self):
        arr = []
        curr = self
        while curr.prev != None:
            curr = curr.prev
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        print(arr)
