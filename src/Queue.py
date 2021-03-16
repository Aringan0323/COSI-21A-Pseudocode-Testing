class Queue:

    def __init__(self, name, data=[]):
        self.q = data
        self.name = name
        self.data_type = 'Queue'

    def enqueue(self, x):
        self.q.append(x)
        self.print('enqueue')

    def dequeue(self):
        popped_item = self.q.pop(0)
        self.print('dequeue')
        return popped_item

    def size(self):
        size = len(self.q)
        print("The size of {} is {}\n".format(self.name, size))
        return size

    def isEmpty(self):
        is_empty = len(self.q) == 0
        print("{} is empty is {}\n".format(self.name, is_empty))
        return is_empty

    def to_string(self):
        return "{}: {}".format(self.name, self.q)

    def print(self, function_name):
        print("After {}, {}: {}\n".format(function_name, self.name, self.q))

def enqueue(Q, x):
    Q.q.append(x)
    Q.print('enqueue')


def dequeue(Q):
    popped_item = Q.q.pop(0)
    Q.print('dequeue')
    return popped_item
