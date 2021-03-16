#!/usr/bin/env python
from LinkedList import Node, DoubleNode
import traceback
import sys
sys.path.insert(0, '../src/')


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
    return L, 4

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
    try:
        cb(L1,n1)
    except:
        print("ERROR OCCURRED WHEN COMPRESSING L1")
        print(traceback.format_exc())
    L1.print('L1 After compression')
    print('\n\n')

    L2.print('L2 Before compression')

    try:
        cb(L2,n2)
    except:
        print("ERROR OCCURRED WHEN COMPRESSING L2")
        print(traceback.format_exc())
    L2.print('L2 After compression')
    print("\n\n")

    print('L3 Before compression\n{}'.format(L3))

    try:
        cb(L3,n3)
    except:
        print("ERROR OCCURRED WHEN COMPRESSING L3")
        print(traceback.format_exc())
    print('L3 After compression\n{}'.format(L3))
    print("\n\n")

    L4.print('L4 Before compression')
    try:
        cb(L4,n4)
    except:
        print("ERROR OCCURRED WHEN COMPRESSING L4")
        print(traceback.format_exc())
    L4.print('L4 After compression')

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

def compress(L, n):

    #Put pseudocode here

    return


LL_test(compress)

#L1 = [1,2,3,4,5,6,7,8,9,10], n1 = 2
#L1 after compression should be = [3,7,11,15,19]

#L2 = = [1,2,3,4,5,6,7,8,9], n2 = 4
#L2 after compression should be = [10,26,9]

#L3 = None, n3 = 1
#L3 after compression should be = None

#L4 = [1,2,3,4,5,6,7,8,9,10], n4 = 15
#L4 after compression should be = [55]
