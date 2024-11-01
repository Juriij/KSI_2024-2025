from typing import List


def solve(positions: List[int], velocities: List[int], queries: List[int]) -> List[List[int]]:

    first_penguins = []  # [[position-indexes]]
    first_penguins_temp = {}  # {query-index: [position-indexes]}
    
    queries_dict = {value: index for index, value in enumerate(queries)} # {query:index} O(q)


    # This loop checks if there are penguins located at all the LOL's possible positions

    visited_queries_iter = set()  # variable that remembers queries visited for each iteration {query_value} 
    for i in range(len(positions)):   # O(n)
        if positions[i] in queries_dict:        
            penguin_index = i
            visited_query_index = queries_dict[positions[i]]

            
            if visited_query_index not in first_penguins_temp:
                first_penguins_temp[visited_query_index] = []  # Initialize with an empty list

            # Make a log that a query has been visited by a peguin on index "penguin_index" == "x"
            first_penguins_temp[visited_query_index].append(penguin_index)

            # Make a log that query has been visited so that it can be popped at the end of iteration
            visited_queries_iter.add(positions[i])
    

    # Sorting penguin indexes
    for key in first_penguins_temp:      # O(q) after all it will run "q" times
        if len(first_penguins_temp[key]) != 1:
            first_penguins_temp[key].sort()

    # Popping visited queries
    for query in visited_queries_iter:   # O(q) after all it will run "q" times
        queries_dict.pop(query)


    # Clearing 
    visited_queries_iter = set()

    # print(f'visited queries: {first_penguins_temp}')
    # print(f'unvisited queries: {queries_dict}')
    

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
