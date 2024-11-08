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
        


# Tuto funkci implementuj.
def is_valid(family_tree: FamilyTree) -> bool:
    pass

# Testy:
# Hláška "Tvůj kód se nepodařilo spustit, oprav si chyby!" môže ľahko znamenať, že padli tieto testy
# ak chcete skúsiť, či to je nimi, len vymažte testy.
tree = FamilyTree(Fish("Goldie0", "Ostriez", 10))
for i in range(1, 10):
    tree.add(Fish("Goldie" + str(i), "Ostriez", i), "Goldie" + str(i - 1))
    tree.add(Fish("NotGoldie" + str(i), "NieOstriez", i), "Goldie" + str(i - 1))

# pouzili sme len add, teda validny strom
assert is_valid(tree)

# pridame meno do
assert not is_valid(tree) _names, pricom sa tam ryba s menom "Oliver" nenachadza
tree._names.add("Oliver")
tree._names.remove("Oliver")

# zvysime hodnotu jednej ryby o 42, preto sub_tree_value nebude spravne nastavene
tree._root.children[0].fish.value += 42
assert not is_valid(tree)
tree._root.children[0].fish.value -= 42

# v strome su dve ryby s rovnakym menom
tree._root.children[0].children.append(Node(tree._root.fish))
assert not is_valid(tree)
tree._root.children[0].children.pop()
