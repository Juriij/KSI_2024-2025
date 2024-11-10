from typing import List, Set, Optional

## DEFINOVANÉ TRIEDY NEMENIŤ
class Fish:
    def __init__(self, name: str, species: str, value: int):
        self.name = name
        self.species = species
        self.value = value

class Node:
    def __init__(self, fish: Fish):
        self.fish = fish
        self.children: List[Node] = []
        self.sub_tree_value = fish.value
    
    def add_aux(self, fish: Fish, parent_name: str) -> bool:
        if self.fish.name == parent_name:
            # ryba nemôže mať potomka iný druh ryby
            if self.fish.species != fish.species:
                return False
            self.children.append(Node(fish))
            self.sub_tree_value += fish.value
            return True
        for child in self.children:
            if child.add_aux(fish, parent_name):
                self.sub_tree_value += fish.value
                return True
        return False

class FamilyTree:
    def __init__(self, root: Fish):
        self._root: Node = Node(root)
        self._names: Set[str] = {root.name}

    def add(self, fish: Fish, parent_name: str):
        if parent_name not in self._names or fish.name in self._names:
            return
        if self._root.add_aux(fish, parent_name):
            self._names.add(fish.name)
        




def check_names(fish_names, fish_name):
    original_len = len(fish_names)
    fish_names.add(fish_name)
    if original_len == len(fish_names):
        return False
    
    return True



# Tuto funkci implementuj.
def is_valid(family_tree: FamilyTree, root=None, fish_names=set(), sub_tree_value_count=0) -> bool:
    if root == None:
        root = family_tree._root
        fish_names = set()
        
    sub_tree_value_count += root.fish.value

    children = root.children

    # check for duplicates (names)
    if check_names(fish_names, root.fish.name) == False:
        return False, 0, 0

    if children == [] and root is not family_tree._root:
        return None, sub_tree_value_count, fish_names
    
    else:
        for child in children:
            if child.fish.species != root.fish.species:
                if root is family_tree._root:
                    return False

                else:
                    return False, 0, 0

            
            validity, sub_tree_value_count, fish_names = is_valid(family_tree, child, fish_names, sub_tree_value_count)

            if validity == False:
                if root is family_tree._root:
                    return False

                else:
                    return False, 0, 0

        
    if root is family_tree._root:  # recursion is over
        # checking sub_tree_value validity for the family_tree._root and '_names' validity  
        if root.sub_tree_value == sub_tree_value_count and len(family_tree._names) == len(fish_names):          
            return True

        else:
            return False
    
    else:
        return None, sub_tree_value_count, fish_names
