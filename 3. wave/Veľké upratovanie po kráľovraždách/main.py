from typing import Set
from value_lib import ValueFactory, Value



def reference_count(vertex):
    # print("the current vertex is: ", vertex.value.get_value())

    if len(vertex.referencing_me) == 0:
        vertex.value.free() 

        for successor in vertex.successors:
            successor.referencing_me.remove(vertex)
            
            reference_count(successor)


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

        penguin.referencing_me.add(self)

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






    def kill(self, name: str) -> None:
        for penguin in self.penguins:
            if penguin.value.get_value() == name:
                self.penguins.remove(penguin)   # kill the connection Country -> Penguin
                
                penguin.referencing_me.remove(self)

                reference_count(penguin)

                break

    


    def has(self, name: str, dest: str) -> 'iterator':
        for penguin in self.penguins:
            if penguin.value.get_value() == name:
                if name != dest:
                    path_found, path_values, path_vertexes = self.find_path(penguin, dest)

                    path_values.insert(0, penguin.value)
                    path_vertexes.insert(0, penguin)

                    return iter(Path(path_found, path_values, path_vertexes))
                
                return iter(Path(True, [penguin.value], [penguin]))

        return iter(Path(False, [], []))





    def find_path(self, node, dest):

        for successor in node.successors:
            if successor.value.get_value() == dest:
                return True, [successor.value], [successor]
            
            path_found, path_values, path_vertexes = self.find_path(successor, dest)

            if path_found:
                path_values.insert(0, successor.value)
                path_vertexes.insert(0, successor)
                return path_found, path_values, path_vertexes
            
        return False, [], []




    def collect(self) -> None:
        pass







class Path:
    def __init__(self, path_found, path_values, path_vertexes):
        if not path_found:
            raise StopIteration

        self.count_ref = -1
        self.count_val = 0
        self.path_values = path_values
        self.path_vertexes = path_vertexes

        for vertex in self.path_vertexes:
            vertex.referencing_me.add(self)


    def __iter__(self):
        return self


    def __next__(self):
        if self.count_ref != -1:
            vertex = self.path_vertexes[self.count_ref]

            vertex.referencing_me.remove(self)  # remove reference

            reference_count(vertex)  # conduct reference counting

            
        if not self.count_val > len(self.path_values)-1:
            value = self.path_values[self.count_val]
        
        else:
            raise StopIteration

        self.count_ref += 1
        self.count_val += 1
        
        return value















# Základné testy
vf = ValueFactory()
c = Country(vf)
c.add_penguin("NieKarlik")
c.add_nonpenguin("NieKarlik", "pocitac")
c.add_penguin("ByvalyKral")
c.add_nonpenguin("ByvalyKral", "sen ovladnut svet")
c.add_nonpenguin("sen ovladnut svet", "vsetky tucniacice")



assert len(vf._values) == 5
assert all([not x._is_disposed for x in vf._values])

c.kill("ByvalyKral")
assert not vf._values[0]._is_disposed
assert not vf._values[1]._is_disposed
assert vf._values[2]._is_disposed
assert vf._values[3]._is_disposed
assert vf._values[4]._is_disposed



# for pingu in c.penguins:
#     print(pingu.value.get_value())




c.add_penguin("ByvalyKral")
c.add_nonpenguin("ByvalyKral", "sen ovladnut svet")
c.add_nonpenguin("sen ovladnut svet", "vsetky tucniacice")


# for pingu in c.penguins:
#     print(pingu.value.get_value())
#     if pingu.value.get_value() == "ByvalyKral":
#         print("is disposed:", pingu.value._is_disposed)




for val in c.has("ByvalyKral", "vsetky tucniacice"):
    if val.get_value() == "sen ovladnut svet":
        c.kill("ByvalyKral")
        assert vf._values[5]._is_disposed
        assert not vf._values[6]._is_disposed
        assert not vf._values[7]._is_disposed

assert vf._values[6]._is_disposed
assert vf._values[7]._is_disposed

c.add_nonpenguin("pocitac", "suciastky")
# trochu hack, lebo sa mnozina neda indexovat
c.add_edge(next(iter(c.penguins)).successors[0].successors[0], 
           next(iter(c.penguins)).successors[0])
c.kill("NieKarlik")

assert vf._values[0]._is_disposed
assert not vf._values[1]._is_disposed
assert not vf._values[8]._is_disposed