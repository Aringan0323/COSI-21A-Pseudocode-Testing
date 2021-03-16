#!/usr/bin/env python
import traceback
import sys
sys.path.insert(0, '../src/')

from LinkedList import Node, DoubleNode
from Test import Test


def even_case():
    L = Node(1)
    curr = L
    for i in range(2, 11):
        curr.next = Node(i)
        curr = curr.next
    return (L, 2)

def odd_case():
    L = Node(1)
    curr = L
    for i in range(2, 10):
        curr.next = Node(i)
        curr = curr.next
    return (L, 4)

def empty_case():
    return (None,1)

def overflow_case():
    L = Node(1)
    curr = L
    for i in range(2, 11):
        curr.next = Node(i)
        curr = curr.next
    return (L, 15)

def create_test_params():
        L1, n1 = even_case()
        L2, n2 = odd_case()
        L3, n3 = empty_case()
        L4, n4 = overflow_case()

        cases_args = [(L1,n1), (L2,n2), (L3,n3), (L4,n4)]

        input_print = [
                ("L1 before compression: ", L1),
                ("L2 before compression: ", L2),
                ("L3 before compression: ", L3),
                ("L4 before compression: ", L4)]

        output_print = [
                ("L1 after compression: ", L1),
                ("L2 after compression: ", L2),
                ("L3 after compression: ", L3),
                ("L4 after compression: ", L4)]
        return cases_args, input_print, output_print

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

cases_args, input_print, output_print = create_test_params()

LL_test = Test(compress_solution, cases_args, input_print, output_print=output_print)

LL_test.run()


#L1 = [1,2,3,4,5,6,7,8,9,10], n1 = 2
#L1 after compression should be = [3,7,11,15,19]

#L2 = = [1,2,3,4,5,6,7,8,9], n2 = 4
#L2 after compression should be = [10,26,9]

#L3 = None, n3 = 1
#L3 after compression should be = None

#L4 = [1,2,3,4,5,6,7,8,9,10], n4 = 15
#L4 after compression should be = [55]
