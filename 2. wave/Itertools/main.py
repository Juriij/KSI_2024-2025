from itertools import combinations, permutations, product, combinations_with_replacement



def create_team(
        empl: list[int],
        team_size: int,
        max_rate: int
        ) -> list[list[int]]:
    
    return [list(comb) for comb in combinations(empl, team_size) if sum(comb) <= max_rate]





employees = [300, 600, 270, 295, 120, 500, 150, 480]
print(create_team(employees, 3, 550))  # [[270, 120, 150]]
print(create_team(employees, 2, 400))  # [[270, 120], [120, 150]]
print(create_team(employees, 2, 100))  # []
