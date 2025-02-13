c.add_penguin("Jurlik")
c.add_nonpenguin("Jurlik", "vsetky tucniacice")





from typing import Set
from value_lib import ValueFactory, Value



def reference_count(vertex, added_set, visited):
    if vertex not in visited and len(vertex.referencing_me) == 0:
        # print("freeing:", vertex)
        vertex.value.free() 
        added_set.remove(vertex)
        
        visited.add(vertex)

        for successor in vertex.successors:
            successor.referencing_me.remove(vertex)
            
            reference_count(successor, added_set, visited)


class Vertex:
    def __init__(self, value: Value):
        self.value = value
        self.successors = []
        self.referencing_me = set()
    
    # # TO BE REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # # TO BE REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # def __repr__(self):s
    #     return f'{self.value.get_value()}'
    
    # # TO BE REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # # TO BE REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Country:
    def __init__(self, value_factory: ValueFactory):
        self.__value_factory = value_factory
        self.penguins = set()

        self.added = set()
        self.referenced_by_iterator = []



    def expand_iter_ref(self, new):
        self.referenced_by_iterator.extend(new)


    def contract_iter_ref(self, removed):
        self.referenced_by_iterator.pop(self.referenced_by_iterator.index(removed))


    def add_penguin(self, name: str) -> None:
        penguin = Vertex(self.__value_factory.make_value(name))

        penguin.referencing_me.add(self)

        self.penguins.add(penguin)
        self.added.add(penguin)

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
            self.added.add(new_vertex)

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
                self.penguins.remove(penguin)   
                
                penguin.referencing_me.remove(self)   # kill the connection Country -> Penguin

                reference_count(penguin, self.added, set())

                break

    


    def has(self, name: str, dest: str) -> 'iterator':
        for penguin in self.penguins:
            if penguin.value.get_value() == name:
                if name != dest:
                    path_found, path_values, path_vertexes = self.find_path(penguin, dest)

                    path_values.insert(0, penguin.value)
                    path_vertexes.insert(0, penguin)

                    return iter(Path(path_found, path_values, path_vertexes, self.expand_iter_ref, self.contract_iter_ref, self.added))
                
                return iter(Path(True, [penguin.value], [penguin], self.expand_iter_ref, self.contract_iter_ref, self.added))

        return iter(Path(False, [], [], self.expand_iter_ref, self.contract_iter_ref, self.added))





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

    
    def search(self, parent, unreachable, visited):
        for vertex in parent.successors:
            if vertex not in visited:
                visited.add(vertex)

                if vertex in unreachable:
                    unreachable.remove(vertex)
                
                self.search(vertex, unreachable, visited)




    def collect(self) -> None:
        unreachable_country = {obj for obj in self.added}

        #print(unreachable_country)

        for parent in self.penguins:
            unreachable_country.remove(parent)
            self.search(parent, unreachable_country, set())

        #print(unreachable_country)

        unreachable_iter = self.added - set(self.referenced_by_iterator)
        #print(unreachable_iter)


        unreachables = unreachable_country & unreachable_iter


        for unreachable in unreachables:

            for friend in unreachable.referencing_me:
                if isinstance(friend, Vertex):
                    friend.successors.pop(friend.successors.index(unreachable))

            unreachable.value.free() 
            
            self.added.remove(unreachable)


            for successor in unreachable.successors:
                successor.referencing_me.remove(unreachable)
                
                setik = unreachables
                reference_count(successor, self.added, setik)














class Path:
    def __init__(self, path_found, path_values, path_vertexes, expand_iter, contract_iter, added):
        if not path_found:
            raise StopIteration

        self.count_ref = -1
        self.count_val = 0
        self.path_values = path_values
        self.path_vertexes = path_vertexes

        self.added = added
        self.contract_iter = contract_iter

        for vertex in self.path_vertexes:
            vertex.referencing_me.add(self)

        expand_iter(self.path_vertexes)

        # for vertex in self.path_vertexes:
        #     print(vertex.value.get_value())


    def __iter__(self):
        return self


    def __next__(self):
        #print(f"I am hererer: current vertex {self.path_values[self.count_val].get_value()}")
       # print("the self.count_ref is:", self.count_ref)
        #print("the self.count_value is:", self.count_val)
        if self.count_ref != -1:
            #print(self.count_ref)
            
            vertex = self.path_vertexes[self.count_ref]

            # print(vertex.value.get_value())

            vertex.referencing_me.remove(self)  # remove reference
            
            self.contract_iter(vertex)

            reference_count(vertex, self.added, set())  # conduct reference counting

            
        if not self.count_val > len(self.path_values)-1:
            value = self.path_values[self.count_val]
        
        else:
            raise StopIteration

        self.count_ref += 1
        self.count_val += 1
        
        return value
