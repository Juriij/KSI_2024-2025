class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def enqueue(self, node):
        if self.tail is not None:
            self.tail.next = node   # linked with the list

        else:
            self.head = node    

        node.next = None
        self.tail = node      # added to the back of the queue


    def dequeue(self):
        if self.head is None:
            return
        
        if self.head.next == None:
            self.tail = None
        
        old_head = self.head
        new_head = self.head.next
        self.head = new_head

        return old_head
        



# Testy:
queue = Queue()
prvy = Node(1)
druhy = Node(2)
treti = Node(3)

# vlozenie prveho Node
queue.enqueue(prvy)
assert queue.head == prvy
assert queue.tail == prvy
assert queue.head.value == 1

# vlozenie druheho Node
queue.enqueue(druhy)
assert queue.head == prvy
assert queue.tail == druhy
assert queue.head.value == 1
assert queue.tail.value == 2

assert queue.head.next == druhy
assert queue.tail.next is None

# vybranie prveho Node
assert queue.dequeue() == prvy
assert queue.head == druhy
assert queue.tail == druhy
assert queue.head.value == 2

assert queue.tail.next is None

# vlozenie tretieho Node
queue.enqueue(treti)
assert queue.head == druhy
assert queue.tail == treti
assert queue.head.value == 2
assert queue.tail.value == 3

assert queue.head.next == treti
assert queue.tail.next is None

# vybranie vsetkeho
assert queue.dequeue() == druhy
assert queue.dequeue() == treti
assert queue.dequeue() is None
assert queue.head is None
assert queue.tail is None
