def csp_solve(
    variables: dict[str, list[str]],
    domains: dict[str, list[str]]
) -> bool:
    
    # arrangment -> point: assigned_value
    assigned_points = dict() 

    if loop_over(variables, domains, assigned_points):
        return True

    return False

    
    




def loop_over(variables, domains, assigned_points):
    # sort variables by len(domains)
    sorted_variables = sorted(variables, key=lambda point: len(domains[point]))
    
    # loop over sorted variables
    for point in sorted_variables:

        if point not in assigned_points:
            if len(domains[point]) == 0:
                assigned_points[point] = True
            
            elif len(domains[point]) == 1:
                assigned_points[point] = domains[point][0]

            else:
                for value in domains[point]:
                    assigned_points[point] = value

                    valid, assigned_points = validate_neighbourhood(point, variables[point], assigned_points, domains)
          
                    if valid:
                        break  

                if valid == False:
                    return False

    return True





def validate_neighbourhood(anchor, neighbourhood, assigned_points, domains):
    for point in neighbourhood:
        if point not in assigned_points:
            assigned_points = assign_value(point, domains, assigned_points)
            
        if is_valid(anchor, point, assigned_points):
            continue
        
        # not valid neighbourhood
        return False, assigned_points
    
    return True, assigned_points
        

        


def is_valid(point1, point2, assigned_points):
    if assigned_points[point1] == True or assigned_points[point2] == True:
        return True
        
    elif assigned_points[point1] != assigned_points[point2]:
        return True

    else:
        return False
    

def assign_value(point, domains, assigned_points):
    assigned_points[point] = domains[point][0]
    return assigned_points














# testy:
print(csp_solve({"A": ["B"], "B": ["A"]},
                {"A": ["makrela"], "B": ["treska"]}))  # True
print(csp_solve({"A": ["B"], "B": ["A"]},
                {"A": ["makrela"], "B": ["makrela"]}))  # False
print(csp_solve({"A": ["B", "C"], "B": ["A", "D"],
                "C": ["A", "D"], "D": ["B", "C"]},
                {"A": ["makrela", "sardinka"], "B": ["makrela", "sardinka"],
                "C": ["makrela", "sardinka"], "D": ["makrela", "sardinka"]}))  # True
print(csp_solve({"A": ["E"], "B": ["E"], "C": ["E"],
                 "D": ["E"], "E": ["A", "B", "C", "D"]},
                {"A": ["losos"], "B": ["losos"], "C": ["losos"],
                "D": ["losos"], "E": ["losos", "treska"]}))  # True
