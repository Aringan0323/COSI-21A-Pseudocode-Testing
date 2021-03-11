import Queue
import Stack

def isEmpty(X):
    if X.data_type == 'Queue':
        is_empty = len(X.q) == 0
        print("{} is empty is {}\n".format(X.name, is_empty))
        return is_empty
    elif X.data_type == 'Stack':
        is_empty = len(X.s) == 0
        print("{} is empty is {}\n".format(X.name, is_empty))
        return is_empty
    return None

def size(X):
    if X.data_type == 'Queue':
        size = len(X.q)
        print("The size of {} is {}\n".format(X.name, size))
        return size
    elif X.data_type == 'Stack':
        size = len(X.s)
        print("The size of {} is {}\n".format(X.name, size))
        return size
    return None
