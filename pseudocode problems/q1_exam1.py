#!/usr/bin/env python
import sys
sys.path.insert(0, '../src/')
from LinkedList import Node, DoubleNode

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

def even_case():
    L = Node(1)
    curr = L
    for i in range(2, 11):
        curr.next = Node(i)
        curr = curr.next
    return L, 2

def odd_case():
    L = Node(1)
    curr = L
    for i in range(2, 10):
        curr.next = Node(i)
        curr = curr.next
    return L, 2

def empty_case():
    return None,1

def overflow_case():
    L = Node(1)
    curr = L
    for i in range(2, 11):
        curr.next = Node(i)
        curr = curr.next
    return L, 15

def testing_example():

    L1, n1 = even_case()
    L2, n2 = odd_case()
    L3, n3 = empty_case()
    L4, n4 = overflow_case()

    L1.print('Before compression')
    L2.print('Before compression')
    print(L3)
    L4.print('Before compression')
    print("\n\n")

    compress(L1,n1)
    compress(L2,n2)
    compress(L3,n3)
    compress(L4,n4)

    L1.print('After compression')
    L2.print('After compression')
    print(L3)
    L4.print('After compression')


testing_example()
