import sys
sys.path.insert(1,"../src/")

from Queue import Queue, dequeue, enqueue
from Stack import Stack, push, pop, top
from QueueStackMethods import isEmpty, size
from LinkedList import Node, DoubleNode


S1 = Stack('S', [1,2,3,4,5])
S2 = Stack('S', [])
S3 = Stack('S', [1,4,2,5,7,5,3])


def mirror_solution(S):
    Q = Queue('Q')
    n = size(S)
    while not isEmpty(S):
        enqueue(Q, pop(S))
    while not isEmpty(Q):
        push(S, dequeue(Q))
    while not isEmpty(S):
        enqueue(Q, top(S))
        enqueue(Q, pop(S))
    for i in range(n):
        push(S, dequeue(Q))
        enqueue(Q, dequeue(Q))
    while not isEmpty(Q):
        push(S, dequeue(Q))
    for i in range(n):
        enqueue(Q, pop(S))
    while not isEmpty(Q):
        push(S, dequeue(Q))
    return S



def mirror_aria(S):
    auxQueue = Queue('q')
    size = S.size()
    while S.isEmpty() != True:
        e = S.pop()
        auxQueue.enqueue(e)
    for i in range(size):
        e = auxQueue.dequeue()
        auxQueue.enqueue(e)
        S.push(e)
    while S.isEmpty() != True:
        e = S.pop()
        auxQueue.enqueue(e)
    for i in range(size):
        e = auxQueue.dequeue()
        auxQueue.enqueue(e)
    while auxQueue.isEmpty() != True:
        e = auxQueue.dequeue()
        S.push(e)
    return S


def mirror_apple(S):
    q = Queue('q')
    n = S.size()
    for i in range(n):
        q.enqueue(S.pop())
    for i in range(n):
        p = q.dequeue()
        q.enqueue(p)
        S.push(p)
    for i in range(n):
        q.enqueue(S.pop())
    for i in range(n):
        q.enqueue(q.dequeue())
    while not isEmpty(q):
        push(S, q.dequeue())
    return S

def mirror(S):
    if isEmpty(S):
        return "empty stack error"
    elif size(S) == 1:
        return S

    originalSize = size(S)
    Q = Queue('q')
    while not isEmpty(S):
        Q.enqueue(S.top())
        Q.enqueue(S.top())

    for i in range(size(Q)):
        S.push(Q.dequeue())
        Q.enqueue(Q.dequeue())

    while isEmpty(S) == False:
        Q.enqueue(S.pop())

    for i in range(originalSize):
        Q.enqueue(S.pop())

    for i in range(size(Q)):
        S.push(Q.dequeue())
    return S





print(mirror(S1).s)
