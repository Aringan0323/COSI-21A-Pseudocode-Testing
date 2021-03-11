from Queue import Queue, dequeue, enqueue
from Stack import Stack, push, pop, top
from QueueStackMethods import isEmpty, size
from LinkedList import Node, DoubleNode
#
# S1 = Stack('S', [1,2,3,4,5])
# S2 = Stack('S', [])
# S3 = Stack('S', [1,4,2,5,7,5,3])
#
#
# def mirror_solution(S):
#     Q = Queue('Q')
#     n = size(S)
#     while not isEmpty(S):
#         enqueue(Q, pop(S))
#     while not isEmpty(Q):
#         push(S, dequeue(Q))
#     while not isEmpty(S):
#         enqueue(Q, top(S))
#         enqueue(Q, pop(S))
#     for i in range(n):
#         push(S, dequeue(Q))
#         enqueue(Q, dequeue(Q))
#     while not isEmpty(Q):
#         push(S, dequeue(Q))
#     for i in range(n):
#         enqueue(Q, pop(S))
#     while not isEmpty(Q):
#         push(S, dequeue(Q))
#     return S
#
#
#
# def mirror_inverted(S):
#     if isEmpty(S):
#         return 'Error of some kind or false'
#     Q = Queue('Q')
#     size = S.size()
#     while not isEmpty(S):
#         enqueue(Q, pop(S))
#     for i in range(0, size):
#         temp = dequeue(Q)
#         push(S, temp)
#         enqueue(Q, temp)
#     while not isEmpty(S):
#         enqueue(Q, pop(S))
#     while not isEmpty(Q):
#         push(S, dequeue(Q))
#
#     return S
#
#
# def mirror(S):
#     Q = Queue('Q')
#     while not isEmpty(S):
#         enqueue(Q, pop(S))
#     for i in range(Q.size(), 0, -1):
#         temp = dequeue(Q)
#         push(S, temp)
#         enqueue(Q, temp)
#     while not isEmpty(S):
#         enqueue(Q, pop(S))
#     while not isEmpty(Q):
#         push(S, dequeue(Q))
#
#     return S
#
# print(mirror(S1))

L = DoubleNode(1)
curr = L
for i in range (2,11):
    curr.next = DoubleNode(i)
    curr.next.prev = curr
    curr = curr.next
L.print()
curr.print()
