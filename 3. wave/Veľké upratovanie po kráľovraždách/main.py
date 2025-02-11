from typing import Set
from value_lib import ValueFactory, Value


class Vertex:
    def __init__(self, value: Value):
        self.value = value
        self.successors = []
        self.referencing_me = set()


class Country:
    def __init__(self, value_factory: ValueFactory):
        self.__value_factory = value_factory
        self.penguins = set()

    def add_penguin(self, name: str) -> None:
        penguin = Vertex(self.__value_factory.make_value(name))
        self.penguins.add(penguin)

    def add_nonpenguin(self, parent: str, value: str) -> None:
        searched: Set[Vertex] = set()
        for penguin in self.penguins:
            if self.__add_nonpenguin_aux(penguin, parent, value, searched):
                break

    def __add_nonpenguin_aux(self, current: Vertex, parent: str, new: str, 
                             searched: Set[Vertex]) -> bool:
        if current in searched:
            return False
        searched.add(current)
        if current.value.get_value() == parent:
            new_vertex = Vertex(self.__value_factory.make_value(new))

            current.successors.append(new_vertex)
            new_vertex.referencing_me.add(current)

            return True
        for vertex in current.successors:
            if self.__add_nonpenguin_aux(vertex, parent, new, searched):
                return True
        return False


    def add_edge(self, first: Vertex, second: Vertex) -> None:
        if second not in first.successors:
            first.successors.append(second)

            second.referencing_me.add(first)



    def reference_count(self, vertex):
        if len(vertex.referencing_me) == 0:
            vertex.value.free() 

            for successor in vertex.successors:
                successor.referencing_me.remove(vertex)
                
                self.reference_count(successor)


    def kill(self, name: str) -> None:
        for penguin in self.penguins:
            if penguin.value.get_value() == name:
                self.penguins.remove(penguin)   # kill the connection Country -> Penguin

                self.reference_count(penguin)

                break

    



    # ?what if name represents vertex that is not part of self.penguins - nonexistent or dead
    # ?what to do if name and dest are identical
    def has(self, name: str, dest: str) -> 'iterator':
        
        for penguin in self.penguins:
            if penguin.value.get_value() == name:
                start_vertex = penguin
                break

        path_found, path = self.find_path(start_vertex, dest)

        return iter(Path(path_found, path))
        



    def find_path(self, node, dest):

        for successor in node.successors:
            if successor.value.get_value() == dest:
                return True, [dest]
            
            path_found, path = self.find_path(successor, dest)

            if path_found:
                path.insert(0, successor.value.get_value())
                return path_found, path
            
        return False, []




    def collect(self) -> None:
        pass




# 1. finish the main purpose of __next__() -> to return the values upon call
# 2. implement the referencing of the vertexes in the path as well as release of a reference upon call
class Path:
    def __init__(self, path_found, path):
        if not path_found:
            raise StopIteration

        self.path = path


    def __iter__(self):
        return self


    def __next__(self):
        # ...
        pass
