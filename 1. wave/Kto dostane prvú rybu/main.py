from typing import List

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
