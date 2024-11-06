from typing import List
from random import seed, randint
import time

# time complexity: O(q*n)
def solve(positions: List[int], velocities: List[int], queries: List[int]) -> List[List[int]]:
    first_penguins = []  # [[position-indexes]]       

    for i in range(len(queries)):
        best_candidates = []
        best_time = 10**20

        for j in range(len(positions)):
            time = abs(queries[i] - positions[j]) / velocities[j]

            if time == best_time:
                best_candidates.append(j)

            elif time < best_time:
                best_candidates = [j]
                best_time = time

        best_candidates.sort()
        first_penguins.append(best_candidates)
            
            

    return first_penguins






# # Toto je príklad pre prvú sadu -- ku každej pozícii pribehne ako prvý iba jediný tučniak
# positions = [28, 95, 0, 98] 
# velocities = [1, 8, 2, 10] 
# queries = [61, 26, 40, 34, 84, 85] 
# print(solve(positions, velocities, queries))
# # [[3], [0], [3], [0], [1], [1]]






# # Toto je príklad pre druhú sadu -- všetky pozície tučniakov sú naľavo od všetkých možností miesta stánku
# positions = [44, 12, 30]
# velocities = [2, 9, 6]
# queries = [77, 78, 59, 66, 61, 80]
# print(solve(positions, velocities, queries))
# # [[1], [1], [2], [1, 2], [2], [1]]