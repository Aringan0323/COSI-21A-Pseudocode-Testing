#!/usr/bin/env python
import sys
sys.path.insert(0,"../src/")

#Import necessary modules
from Queue import Queue, dequeue, enqueue
from Stack import Stack, push, pop, top
from QueueStackMethods import isEmpty, size
from LinkedList import Node, DoubleNode
from Test import Test

# Refer to the README.md file for instructions on how to use this package

def foo_solution():

    # Put the solution to the problem here to compare

    return

def create_test_params():

    # If you want to use the Test class, create a function here
    # to initialize your test cases and create the params. Return
    # the params as a tuple.

    return (,)

def foo():

    # Put the pseudocode you are testing here

    return


# Initialize your test parameters
test_params = create_test_params()

# Initialize a Test object with your function and test parameters
foo_test = Test(foo, *test_params)

# Run the test
foo_test.run()
