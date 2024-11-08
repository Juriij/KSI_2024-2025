from typing import Optional
## DEFINOVANÉ TRIEDY NEMENIŤ
class Fish:
    def __init__(self, name: str, species: str, value: int):
        self.name = name
        self.species = species
        self.value = value

class Node:
    def __init__(self, fish: Fish):
        self.fish = fish
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class Record:
    def __init__(self):
        self._first: Optional[Node] = None
        self._last: Optional[Node] = None
    
    def append(self, fish: Fish) -> None:
        node = Node(fish)
        if self._first is None:
            self._first = node
            self._last = node
            return
        self._last.next = node
        node.prev = self._last
        self._last = node

    def pop(self) -> Optional[Fish]:
        if self._first is None:
            return None
        node = self._last
        if self._first is self._last:
            self._first = None
            self._last = None
            return node.fish
        node.prev.next = None
        self._last = node.prev
        return node.fish
        
        
    
    def popleft(self) -> Optional[Fish]:
        if self._first is None:
            return None
        node = self._first
        if self._first is self._last:
            self._first = None
            self._last = None
            return node.fish
        node.next.prev = None
        self._first = node.next
        return node.fish





def print_nodes(record):
    node = record._first
    
    iter = 0
    while node != None:
        iter += 1
        print(f'{iter}.node: ', node)

        node = node.next
        


def is_duplicate(all_objects, node) -> bool:
    original_length = len(all_objects)
    all_objects.add(node)
    if original_length == len(all_objects): 
        return True




# loop that iterates over the doubly-linked list and checks it's validSity
def record_invalid(record) -> bool:
    all_objects = set()
    node = record._first
    prev_node = node.prev

    while True:   
        if node == None:
            if prev_node is record._last:
                return False
            else:
                return True
            
        if node.prev is not prev_node:
            return True
        
        if is_duplicate(all_objects, node):
            return True


        prev_node = node
        node = node.next




# Tuto funkci implementuj.
def is_valid(record: Record) -> bool:
    # edge case zero elements
    if record._first == None or record._last == None:
        if record._first == None and record._last == None:
            return True
        else:
            return False

    # edge case one element
    if record._last is record._first:
        if record._last.next == None and record._last.prev == None:
            return True
        elif record._first.next == None and record._first.prev == None:
            return True
        else:
            return False
 
    # regular cases:
    if not ( (record._first.prev == None) and (record._last.next == None) ):
        return False

    if record_invalid(record):
        return False

    return True
