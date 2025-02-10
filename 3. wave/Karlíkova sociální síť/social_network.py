from abc import ABC
from collections import deque

class Animal(ABC):
    def __init__(self, name, university_num):
        self.name = name
        self.university_num = university_num
        self.friends = set()

    def __repr__(self):
        return f'Ahoj, já jsem {self.name}!'
    
    def __hash__(self):
        return hash((self.university_num, self.name))
    

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.university_num == other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        

    def __ne__(self, other):
        if isinstance(other, Animal):
            return self.university_num != other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")


    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.university_num < other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")


    def __le__(self, other):
        if isinstance(other, Animal):
            return self.university_num <= other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        


    def __gt__(self, other):
        if isinstance(other, Animal):
            return self.university_num > other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        


    def __ge__(self, other):
        if isinstance(other, Animal):
            return self.university_num >= other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")





class Student(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (100000 <= self.university_num <= 700000):
            raise ValueError("Error, id should be in the range 100 000 - 700 000.")
        

class AkademickyPracovnik(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (700001 <= self.university_num <= 999999):
            raise ValueError("Error, id should be in the range 700 001 - 999 999.")
        



class Host(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (self.university_num >= 1000000):
            raise ValueError("Error, id should be greater or equal to 1 000 000.")




class University:
    def __init__(self):
        self.users = []


    def add_user(self, new_user):
        for user in self.users:
            if user.name == new_user.name and user.university_num == new_user.university_num:
                raise Exception("Error, this user already exists")

        self.users.append(new_user)


    def in_database(self, Users):
        passed = False

        copied_Users = [user for user in Users] # copy

        for user in self.users:
            if user in copied_Users:
                copied_Users.pop(copied_Users.index(user))

            if copied_Users == []:
                passed = True
                break

        if not passed:
            raise Exception("Error, not all the users are added to the database")


    def connect(self, A, B):
        self.in_database([A, B])

        if isinstance(A, Host):
            if not isinstance(B, AkademickyPracovnik):
                raise Exception("Error, Host can be friends only with Academic Worker")

        elif isinstance(B, Host):
            if not isinstance(A, AkademickyPracovnik):
                raise Exception("Error, Host can be friends only with Academic Worker")

        A.friends.add(B)
        B.friends.add(A)
            

    def disconnect(self, A, B):
        self.in_database([A, B])
        A.friends.remove(B)
        B.friends.remove(A)


    def get_friends(self, A):
        self.in_database([A])
        return A.friends
    

    def common_friends(self, Users):
        if len(set(Users)) != len(Users):
            raise Exception("Error, duplicate in the input list. Can't compare common friends of two identical objects")

        self.in_database(Users)
        
        if not Users:
            return set() 
        
        return set.intersection(*(user.friends for user in Users))
    


    def find_path(self, A, B, depth, lengths, visited):
        if A in visited:
            return lengths  

        visited.add(A)

        for friend in A.friends:
            if friend is B:
                lengths.add(depth)
                return lengths  

            self.find_path(friend, B, depth + 1, lengths, visited)

        return lengths



    def find_connection(self, A, B):
        self.in_database([A, B])  

        lengths = self.find_path(A, B, 0, set(), set())  

        return -1 if not lengths else min(lengths)


    


    def is_connected(self):
        if not self.users:
            return False  

        visited = set()
        queue = deque([self.users[0]])  

        while queue:
            user = queue.popleft()
            if user not in visited:
                visited.add(user)
                for friend in user.friends:
                    if friend not in visited:
                        queue.append(friend)

        return len(visited) == len(self.users)
    

    def bfs_shortest_paths(self, start_user):
        distances = {start_user: 0}
        queue = deque([(start_user, 0)])  

        while queue:
            user, dist = queue.popleft()
            for friend in user.friends:
                if friend not in distances:
                    distances[friend] = dist + 1 if user != start_user else 0
                    queue.append((friend, distances[friend]))

        return distances

    def find_diameter(self):
        diameter = 0

        for user in self.users:
            distances = self.bfs_shortest_paths(user)
            valid_distances = [distances[friend] for friend in distances if friend != user]
            if not valid_distances:
                continue
            max_distance = max(valid_distances)
            if max_distance > diameter:
                diameter = max_distance

        return diameter

    def check_hypothesis(self):
        if not self.is_connected():
            return -1

        return self.find_diameter()
