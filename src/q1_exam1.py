#!/usr/bin/env python


from Queue import Queue, dequeue, enqueue
from Stack import Stack, push, pop, top
from QueueStackMethods import isEmpty, size
from LinkedList import Node, DoubleNode

'''
Note:
When using stacks and queues, you can use dot
notation or static method notation to do the same thing.

Ex:
Let Q be a Queue
Q.dequeue() is equivalent to dequeue(Q)
Q.enqueue(x) is equivalent to enqueue(Q)

This works for all stack methods, and methods shared between stacks
and queues such as isEmpty and size
'''
def compress(L, n):
    if L == None:
        return None
    curr = L
    runner = curr
    i = 0
    sum = 0
    while curr != None:
        if i < n and runner != None:
            sum = sum + runner.data
            runner = runner.next
            i += 1
        else:
            curr.data = sum
            curr.next = runner
            curr = runner
            sum = 0
            i = 0


def compress_natalie(L, n):
    x = L
    if x.data == None or x.next == None:
        return L
    while x.next != None:
        i = 0
        if i < (n-1):
            print("IF statement")
            x.print()
            x.data = x.data + x.next.data
            x = x.next
            i = i+1
        else:
            print('ELSE statement')
            x.print()
            i = 0
            x = x.next


def compress_emma(L, n):
    if L == None:
        return l
    counter = 1
    curr = L
    L2 = Node()
    while curr != None:
        curr = curr.next
        counter = counter +1
    curr = L
    sum = 0
    if counter <= n:
        while curr != None:
            sum = curr.data + sum
            curr = curr.next
    else:
        modulo = counter % n
        for i in range(n):
            print("For loop pass {}".format(i))
            L.print()
            sum = curr.data + sum
            curr = curr.next
        curr.data = sum
        L2 = curr

        if modulo != 0:
            curr = curr.next
            for i in range(modulo+1):
                curr.next.data = curr.data + curr.next.data
                curr = curr.next


def compress_john(L, n):
    if L == None:
        return L
    x = L
    size = 0

    while x != None:
        x = x.next
        size = size+1
    if n >= size:
        first = L
        m = first.next
        while m != None:
            first.data = first.data + m.data
            m = m.next
        first.next = None
        return L

    # x = L
    # while x != None:
    #     sum = 0
    #     itr = x.next
    #         sum = sum + itr.data
    #         itr = itr.next
    #     x.data = sum
    #     x = itr


def compress_jason(L, n):
    if L == None:
        return L
    currNode = L
    L.print(125)
    while currNode != None:
        newsum = currNode.data
        L.print(128)
        for i in range(n):
            nextNode = currNode.next
            L.print(131)
            if nextNode != None:
                newsum = newsum + nextNode.data
                L.print(135)
                currNode = nextNode
                L.print(137)
        newNode = Node()
        newNode.data = newsum
        newNode.next = currNode.next
        L.print(141)
        currNode = currNode.next
        L.print(143)
        currNode = newNode.next
        L.print(145)
    return L


def even_case():
    L = Node(1)
    for i in range(2, 11):
        curr.next = Node(i)
        curr = curr.next
    return L, 2

def odd_case():
    L = Node(1)
    for i in range(2, 10):
        curr.next = Node(i)
        curr = curr.next
    return L, 2


def empty_case():
    return None

def overflow_case():
    L = Node(1)
    for i in range(2, 11):



L_regular, n_regular = Node(1), 2
curr = L
for i in range(2, 11):
    curr.next = Node(i)
    curr = curr.next

L_empty = None

L

compress_jason(L, 2)

L.print('final')
