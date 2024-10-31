from typing import List


def solve(positions: List[int], velocities: List[int], queries: List[int]) -> List[List[int]]:
    first_penguins = []
    first_penguins_temp = {}  # {query-index: [position-indexes]}
    
    queries = {value: index for index, value in enumerate(queries)} # {query:index} O(q)


    # This loop checks if there are penguins located at all the LOL's possible positions
    for i in range(len(positions)):   # O(n)
        if positions[i] in queries:
            penguin_index = i
            visited_query_index = queries[positions[i]]


            if visited_query_index not in first_penguins_temp:
                first_penguins_temp[visited_query_index] = {positions[i]: []}  # Initialize with an empty list

            # Now append the penguin_index safely
            first_penguins_temp[visited_query_index][positions[i]].append(penguin_index)
    

    for key in first_penguins_temp:   # popping visited queries 
        for key in first_penguins_temp[key]:
            queries.pop(key)
    


    print(f'these are penguins that arrived: {first_penguins_temp}')
    print(f'these are yet unvisited queries: {queries}')
    
    return first_penguins


                
# Testy:
positions = [28, 95, 0, 98, 28] 
velocities = [1, 8, 2, 10] 
queries = [28, 26, 40, 34, 98, 85] 
solve(positions, velocities, queries)





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
