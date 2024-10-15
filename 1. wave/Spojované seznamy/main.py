class Node:
    """Třída `Node` představuje prvek našich seznamů."""
    def __init__(self, value = None) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        """Inicializuje prázdný seznam"""
        self.first: Node | None = None
        self.last: Node | None = None

    def push_front(self, node: Node) -> None:
        """Přidá prvek `node` na začátek seznamu."""
        node.next = self.first
        self.first = node
        if self.last is None:
            self.last = node

    def push_back(self, node: Node) -> None:
        """Přidá prvek `node` na konec seznamu."""
        if self.last is None:
            self.first = node
        else:
            self.last.next = node
        self.last = node

    def insert_after(self, where_node: Node, what_node: Node) -> None:
        """Vloží prvek `what_node` za prvek `where_node` (na šipku mezi `where_node` a `where_node.next`)."""
        what_node.next = where_node.next
        where_node.next = what_node
        if self.last == where_node:
            self.last = what_node

    def delete_after(self, node: Node) -> None:
        """Odstraní prvek, který se nachází za prvkem `node`

        Pokud je `node` posledním prvkem seznamu, tato metoda nic neudělá. Pokud
        je `node.next` posledním prvkem seznamu, musíme upravit `last`.
        """
        
        if node.next == None:
            return
        
        elif node.next.next == None:
            self.last = node
        
        node.next = node.next.next
        
        


    def to_string(self) -> str:
        """Vrátí stav seznamu jako řetězec.

        Toto je pomocná funkce, která ti může pomoct při hledání chyb.
        """
        if self.first is None:
            return "(empty list)"
        out = "("
        node = self.first
        while node is not None:
            out += "(" + str( node.value ) + ")"
            out += " -> "
            node = node.next
        return out + "None)"


# Testy

l1 = LinkedList()
print( l1.to_string() )

n1 = Node( 1 )
l1.push_front( n1 )
print( l1.to_string() )

n2 = Node( 2 )
l1.push_back( n2 )
print( l1.to_string() )

n3 = Node( 3 )
l1.push_front( n3 )
print( l1.to_string() )

n4 = Node( 4 )
l1.push_front( n4 )
print( l1.to_string() )

n5 = Node( 5 )
l1.insert_after( n4, n5 )
print( l1.to_string() )


l1.delete_after( n3 )
print( l1.to_string() )
