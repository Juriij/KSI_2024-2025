from typing import List

def pop_visited_queries(visited_queries, queries_dict):
    for query in visited_queries:   # O(q) after all it will run "q" times
        queries_dict.pop(query)     # O(1)


def sort_penguins(visited_queries):
    # Sorting penguin indexes
    for key in visited_queries:        # O(q) after all it will run "q" times
        for s_key in visited_queries[key]:   # O(1)
            if len(visited_queries[key][s_key]) != 1:
                visited_queries[key][s_key].sort()     






def move_penguins(init_run, positions, velocities, queries_dict, visited_queries_global, iter):

    visited_queries_local = dict()

    if init_run:
        # This loop checks if there are penguins located at all the marketplace's possible positions
        for i in range(len(positions)):   # O(n)
            if positions[i] in queries_dict:  
                penguin_index = i
                visited_query = positions[i]

                if visited_query not in visited_queries_local:
                    visited_queries_local[visited_query] = {0: []}
                
                visited_queries_local[visited_query][0].append(penguin_index)


    else:
        for i in range(len(positions)):  # iterates over all the penguins O(n)
            start = positions[i] + 1
            end = start + velocities[i]

            for j, step_ahead in enumerate(range(start, end)):  # moves a penguin step by step in both directions
                step_back = start - j - (2*iter)

    
                # has the penguin arrived to a marketplace?
                if step_ahead in queries_dict:   # forward motion     
                    time = (step_ahead - start) / velocities[i]    # time <= 1sec


                    
                    if step_ahead not in visited_queries_local:
                        visited_queries_local[step_ahead] = {time: [i]}
                    
                    else:
                        if min(visited_queries_local[step_ahead].keys()) == time:
                            visited_queries_local[step_ahead][time].append(i)
                        
                        elif min(visited_queries_local[step_ahead].keys()) > time:
                            visited_queries_local[step_ahead] = {time: [i]}
                

                if step_back in queries_dict:     # backward motion
                    time = (start - step_back) / velocities[i]   # time <= 1sec
                
                    

                    if step_back not in visited_queries_local:
                        visited_queries_local[step_back] = {time: [i]}

                    else:
                        if min(visited_queries_local[step_back].keys()) == time:
                            visited_queries_local[step_back][time].append(i)
                        
                        elif min(visited_queries_local[step_back].keys()) > time:
                            visited_queries_local[step_back] = {time: [i]}


        

            positions[i] = end       # update penguin's position after he finished his move



    pop_visited_queries(visited_queries_local, queries_dict)

    for query in visited_queries_local:
        visited_queries_global[query] = visited_queries_local[query]


    return visited_queries_global








def solve(positions: List[int], velocities: List[int], queries: List[int]) -> List[List[int]]:

    first_penguins = []  # [[position-indexes]]        
    visited_queries = dict()     # {query: {shortest_time: [penguins' indexes]}}
    
    queries_dict = {value: index for index, value in enumerate(queries)}            #{query:index} O(q)
    queries_dict_reversed = {index: value for value, index in queries_dict.items()} #{index:query} O(q)
    
    init_run = True 

    iter = 0

    while queries_dict != dict():   
        iter += 1   
        visited_queries = move_penguins(init_run, positions, velocities, queries_dict, visited_queries, iter)
        init_run = False


    # sort penguins' indexes
    sort_penguins(visited_queries)
  
    # transfer "visited_queries" to "first_penguins"
    for i in range(len(queries)):      # O(q)
        query = queries_dict_reversed[i]
        for s_key in visited_queries[query]:
            penguins_indexes = visited_queries[query][s_key]

        first_penguins.append(penguins_indexes)


    return first_penguins
