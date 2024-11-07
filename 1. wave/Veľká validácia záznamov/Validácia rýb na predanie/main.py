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





def record_iterate(record):
    node = record._first
    
    iter = 0
    while node != None:
        iter += 1
        print(f'{iter}.node: ', node)

        node = node.next
        


def check_duplicate(all_objects, node):
    original_length = len(all_objects)
    all_objects.add(node)
    if original_length == len(all_objects):
        return True




# loop that iterates over the doubly-linked list and checks it's validity
def record_invalid(record) -> bool:
    all_objects = set()
    node = record._first

    # first node               ???
    if not type(node.next) == Node:
        return True
    
    #iter = 0        ####################
    while node != None:

        #iter += 1                ################

        # print("iteration: ", iter)    #############
        # print("node.prev: ", node.prev)
        # print("node: ", node)
        # print("node.next: ", node.next)


        if node is record._first:
            all_objects.add(node)

        else:
            if node is not record._last:  # arbitrary node
                if not type(node) == Node:
                    return True
                
                if check_duplicate(all_objects, node.prev):
                    return True
                if check_duplicate(all_objects, node.next):
                    return True
                  

            else:  # last node
                if check_duplicate(all_objects, node):
                    return True
                if check_duplicate(all_objects, node.prev):
                    return True
                if not type(node.prev) == Node:
                    return True


        node = node.next
    
    return False




# Tuto funkci implementuj.
def is_valid(record: Record) -> bool:
    #print(0)
    # edge case zero elements
    if record._first == None or record._last == None:
        if record._first == None and record._last == None:
            return True
        else:
            return False

    #print(1)
    # edge case one element
    if record._last is record._first:
        if record._last.next == None and record._last.prev == None:
            return True
        elif record._first.next == None and record._first.prev == None:
            return True
        else:
            return False
 
    #print(2)
    # regular cases:
    if not ( (record._first.prev == None) and (record._last.next == None) ):
        return False

    #print(3)
    if record_invalid(record):
        return False

    #print(4)
    return True

    

    















# Testy:
# Hláška "Tvůj kód se nepodařilo spustit, oprav si chyby!" môže ľahko znamenať, že padli tieto testy
# ak chcete skúsiť, či to je nimi, len vymažte testy.
test_record = Record()
for i in range(4):
    test_record.append(Fish("Goldie" + str(i), "Ostriez", 10))
test_record.pop()
test_record.popleft()

# pouzili sme len "verejne" metody, tak je to urcite validne
assert is_valid(test_record)

# siahli sme na _last a zmenili ho nespravne, uz nie valid
test_record._last.next = test_record._last
assert not is_valid(test_record)
test_record._last.next = None

#jednosmerne sme zmenili poradie, nie valid
record_iterate(test_record)
test_record._last.prev.prev.prev.next = test_record._last.prev
assert not is_valid(test_record)
test_record._last.prev.prev.prev.next = test_record._last.prev.prev



test_record = Record()
test_record._first = Fish("zuzu", "salmon", 5)
assert not is_valid(test_record)


test_record = Record()
test_record.append(Fish("zuzu", "salmon", 5))
test_record._last.next = Fish("zuzu", "salmon", 5)
assert not is_valid(test_record)
