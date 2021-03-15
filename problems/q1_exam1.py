#!/usr/bin/env python
import sys
sys.path.insert(0, '../src/')
from LinkedList import Node, DoubleNode

def compress_solution(L, n):
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

def LL_test(cb):

    L1, n1 = even_case()
    L2, n2 = odd_case()
    L3, n3 = empty_case()
    L4, n4 = overflow_case()

    L1.print('L1 Before compression')
    cb(L1,n1)
    L1.print('L1 After compression')
    print('\n\n')

    L2.print('L2 Before compression')
    cb(L2,n2)
    L2.print('L2 After compression')
    print("\n\n")

    print('L3 Before compression\n{}'.format(L3))
    cb(L3,n3)
    print('L3 After compression\n{}'.format(L3))
    print("\n\n")

    L4.print('L4 Before compression')
    cb(L4,n4)
    L4.print('L4 After compression')


def compress(L, n):

    #Insert code here

    return




LL_test(compress)
