from typing import Callable, List, Optional, Tuple

# DEFINOVANÉ TRIEDY NEMENIŤ
class Customer:
    # udaje nie su unikatne
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class HashTable:
    # mozete predpokladat, ze obor hodnot hash_function je [0, capacity - 1]
    # az na specialny pripad capacity < 1, kde hash vzdy vrati None
    def __init__(self, hash_function: Callable[[Customer], int], capacity: int):
        self._hash_function = hash_function
        self._table: List[Optional[Tuple[Customer, int]]] = [None for i in range(capacity)]

    def add(self, customer: Customer) -> None:
        index = self._hash_function(customer)
        for i in range(index, index + len(self._table)):
            if self._table[i % len(self._table)] is None:
                self._table[i % len(self._table)] = (customer, 0)
                return
            if self._table[i % len(self._table)][0] is customer:
                return
    
    def increment(self, customer: Customer, count: int):
        if count < 0:
            return
        index = self._hash_function(customer)
        for i in range(index, index + len(self._table)):
            if self._table[i % len(self._table)] is None:
                return
            customer2, points = self._table[i % len(self._table)]
            if customer2 is customer:
                self._table[i % len(self._table)] = (customer, points + count)
                return






# checking if every object is unique and if customers' points are positive ints
def iter_check(hash_table):
    table = hash_table._table
    all_objects = set()

    for i in range(len(table)):
        if not table[i] == None:
            original_length = len(all_objects)
            all_objects.add(table[i][0])
            if original_length == len(all_objects):
                return False
            
            if table[i][1] < 0:
                return False




# checking if the hash table's arrangment is correct
def recursive_check(hash_table, iter_range, valid, invalid, delved):
    table = hash_table._table
    hash_function = hash_table._hash_function

    for i in range(*iter_range):
        if delved:
            if table[i % len(table)] == None:     
                return False, [], []

        if not table[i % len(table)] == None:      
            index = i
            customer = table[index % len(table)][0]  
            hash = hash_function(customer)

            if (customer in valid) or (hash == index % len(table)):
                pass

            else:
                if customer in invalid:
                    return False, [], []
                
                invalid.append(customer)

                if hash < index:
                    iter_range = (hash, index % len(table))

                else:    # hash is greater than index
                    iter_range = (hash, hash + (len(table)-hash) + (index % len(table)))
                

                validity, valid, invalid = recursive_check(hash_table, iter_range, valid, invalid, True)
                
                if validity == False:
                    return False, [], []

                valid.append(invalid.pop())



    return None, valid, invalid





# Tuto funkci implementuj.
def is_valid(hash_table: HashTable) -> bool:
    if len(hash_table._table) == 0:
        return True
    
    if iter_check(hash_table) == False: 
        return False
    
    if len(hash_table._table) == 1:
        return True
    
    validity, _, _ = recursive_check(hash_table, (0, len(hash_table._table)), [], [], False)
        
    if validity == False:
        return False
    
    return True
