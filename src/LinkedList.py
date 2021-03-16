class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


    # Returns all nodes after this one in the linked list as a string
    def to_string(self):
        arr = []
        curr = self
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        return "{}".format(arr)


    # Prints all nodes after this one in the linked list, and the line number
    def print(self, line_num):
        print("Line {}".format(line_num) + ": " + self.to_string())

    # Returns the size of the linked list beginning at this node.
    # Note: This is not a traditional linked list operation, but that
    # doesn't stop students from trying to use it!
    def size(self):
        L = self
        curr = L
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        return count

class DoubleNode:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    # Returns all of the nodes in the linked list
    # that this node is in starting from the beginning as a string
    def to_string(self):
        arr = []
        curr = self
        while curr.prev != None:
            curr = curr.prev
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        return "{}".format(arr)


    # Prints all of the nodes in the linked list
    # that this node is in starting from the beginning as a string,
    # and the line number
    def print(self, line_num):
        print("Line {}".format(line_num) + ": " + self.to_string())

    # Returns the size of the linked list that this node is contained in.
    # Note: This is not a traditional linked list operation, but that
    # doesn't stop students from trying to use it!
    def size(self):
        arr = []
        curr = self
        while curr.prev != None:
            curr = curr.prev
        while curr != None:
            arr.append(curr.data)
            curr = curr.next
        return len(arr)
