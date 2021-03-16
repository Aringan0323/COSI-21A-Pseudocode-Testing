import sys
sys.path.insert(1,"../src/")

from Queue import Queue, dequeue, enqueue
from Stack import Stack, push, pop, top
from QueueStackMethods import isEmpty, size
from Test import Test


def create_test_params():
    S1 = Stack('S', [1,2,3,4,5])
    S2 = Stack('S', [])
    S3 = Stack('S', [5,4,3,2,1])
    S4 = Stack('S', [-1,-2,-3,-4,-5])

    cases_args = [(S1,), (S2,), (S3,), (S4,)]

    input_print = [
            ("S1 before mirror: ", S1),
            ("S2 before mirror: ", S2),
            ("S3 before mirror: ", S3),
            ("S4 before mirror: ", S4)
    ]

    output_print = [
            ("S1 after mirror: ", S1),
            ("S2 after mirror: ", S2),
            ("S3 after mirror: ", S3),
            ("S4 after mirror: ", S4)
    ]

    return cases_args, input_print, output_print

def mirror_solution(S):
    Q = Queue('Q')
    n = size(S)
    while not isEmpty(S):
        #Loads all elements from stack to queue
        enqueue(Q, pop(S))
    while not isEmpty(Q):
        #Loads elements back from queue to stack, reversing the stack
        push(S, dequeue(Q))
    while not isEmpty(S):
        #Loads elements from stack to queue s.t. each element is duplicated
        enqueue(Q, top(S))
        enqueue(Q, pop(S))
    for i in range(n):
        #Pushes one of the duplicates from the queue to the stack, then enqueues
        #the next element in the queue to the end of the queue
        push(S, dequeue(Q))
        enqueue(Q, dequeue(Q))
    while not isEmpty(Q):
        #Pushes all elements from the queue to the stack
        push(S, dequeue(Q))
    for i in range(n):
        #Enqueues half of the elements in the stack into the queue
        enqueue(Q, pop(S))
    while not isEmpty(Q):
        #Pushes all of the elements from the queue to the stack, reversing the order
        push(S, dequeue(Q))
    return S

def mirrorFill(s1, s2):
    while not isEmpty(s2):
        x = s2.pop()
        s1.push(x)
        mirrorFill(s1,s2)
        s1.push(x)
    return s1

def reverseFill(s1):
    s2 = Stack('s2')
    while not isEmpty(s1):
        s2.push(s1.pop())

    return mirrorFill(s1, s2)


cases_args, input_print, output_print = create_test_params()

mirror_test = Test(mirror_solution, cases_args, input_print, output_print)

mirror_test.run()
