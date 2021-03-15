# COSI-21A-Pseudocode-Testing
### Written in python to test problem set solutions written in pseudocode for stacks, queues, and linked lists


## Usage

When testing a new pseudocode problem, make a copy of <code>skeleton.py</code> which is provided in the <code>problems</code>
folder. This file has all of the necessary imports that you will need to get started with testing a pseudocode quesiton, but you may remove unnecessary imports if you wish. Make surethat the new file you create is in the <code>problems</code> folder, or that the path specified is to the <code>src</code> folder.

## About Stacks and Queues

- The Stacks and the Queues are implemented with python lists.
- For each operation that is done on a Stack or a Queue, a message will be printed to the terminal that shows the name
of the Stack or Queue, the operation that is being done to the Stack or Queue, and the elements in the Stack or Queue after
the operation has completed.

## Stacks

* **initializing an empty Stack**: Use <code>Stack = Stack('stack_name')</code> to initialize a new empty Stack
* **initializing a Stack with a list**: Use <code>Stack = Stack('stack_name', [1,2,3])</code> to initialize a Stack with a list 
* **push**: Use <code>push(Stack, element)</code> or <code>Stack.push(element)</code> to push a new element to the top of the Stack
* **top**: Use <code>top(Stack)</code> or <code>Stack.top()</code> to return the last element that was pushed to the Stack
* **pop**: Use <code>pop(Stack)</code> or <code>Stack.pop()</code> to remove and return the last element that was pushed to the Stack
* **isEmpty**: Use <code>isEmpty(Stack)</code> or <code>Stack.isEmpty()</code> to return a boolean value indicating whether or not the Stack is empty
* **size**: Use <code>size(Stack)</code> or <code>Stack.size()</code> to return an integer indicating the size of the Stack.

## Queues

* **initializing an empty Queue**: Use <code>Queue = Queue('queue_name')</code> to initialize a new empty Queue
* **initializing a Queue with a list**: Use <code>Queue = Queue('queue_name', [1,2,3])</code> to initialize a Queue with a list 
* **enqueue**: Use <code>enqueue(Queue, element)</code> or <code>Queue.enqueue(element)</code> to insert a new element in the back of the Queue
* **dequeue**: Use <code>dequeue(Queue)</code> or <code>Queue.dequeue()</code> to remove and return the element at the front of the Queue
* **isEmpty**: Use <code>isEmpty(Queue)</code> or <code>Queue.isEmpty()</code> to return a boolean value indicating whether or not the Queue is empty
* **size**: Use <code>size(Queue)</code> or <code>Queue.size()</code> to return an integer indicating the size of the Queue.


## Linked Lists

* **initializing a new Node**: Use <code>LinkedListNode = Node()</code> to initialize a new empty Node, or <code>LinkedListNode = Node(data)</code> to initialize
a new Node with data.
* **initializing a new DoubleNode**: Use <code>LinkedListNode = DoubleNode()</code> to initialize a new empty DoubleNode, or <code>LinkedListNode = DoubleNode(data)</code>
to initialize a new DoubleNode with data.
* **next**: Use <code>LinkedListNode.next</code> to return the node that is next to the referenced node in a Linked List. Can be used to reassign next pointers
to other nodes.
* **prev**: Only works for Linked Lists containing DoubleNode nodes. Use <code>LinkedListNode.prev</code> to return the node that is before the referenced
node in a Linked List of DoubleNode nodes. Can be used to reassign prev pointers to other nodes.
* **print for Linked Lists of Node nodes**: Use <code>LinkedListNode.print(line_number)</code> to print a list containing the data of every node after the referenced node in
the Linked List. This function will also print out the line number of your choosing.
* **print for Linked Lists of DoubleNode nodes**: Use <code>LinkedListNode.print(line_number)</code> to print a list containing the data of every node in the Linked List containing the referenced node, even if the referenced node is not the first node in the Linked List. This function will also print out the line number of your choosing.
