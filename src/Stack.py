class Stack:

    def __init__(self, name, data=[]):
        self.s = data
        self.name = name
        self.data_type = 'Stack'

    def push(self, x):
        self.s.append(x)
        self.print('push')

    def top(self):
        self.print('top')
        return self.s[-1]

    def pop(self):
        popped_item = self.s.pop(-1)
        self.print('pop')
        return popped_item

    def size(self):
        size = len(self.s)
        print("The size of {} is {}\n".format(self.name, size))
        return size

    def isEmpty(self):
        is_empty = len(self.s) == 0
        print("{} is empty is {}\n".format(self.name, is_empty))
        return is_empty

    def print(self, function_name):
        print("After {}, {}: {}\n".format(function_name, self.name, self.s))

def push(S, x):
    S.s.append(x)
    S.print('push')

def top(S):
    S.print('top')
    return S.s[-1]

def pop(S):
    popped_item = S.s.pop(-1)
    S.print('pop')
    return popped_item
