class Grid2D:
    def __init__(self, values: list[list[int]]) -> None:
        self.height = len(values)
        self.width = len(values[0])
        self.grid = values


    def __repr__(self):
        return f'grid: {self.grid}'


    def __add__(self, other):
        if (self.width >= other.width) and (self.height >= other.height):
            return Grid2D([[other.grid[i][j] + self.grid[i][j] for j in range(other.width)] for i in range(other.height)])            
        
        elif (self.width < other.width) and (self.height < other.height):
            return Grid2D([[other.grid[i][j] + self.grid[i][j] for j in range(self.width)] for i in range(self.height)])


        else:
            iterate_width = self.width if self.width <= other.width else other.width
            iterate_height = self.height if self.height <= other.height else other.height
            return Grid2D([[other.grid[i][j] + self.grid[i][j] for j in range(iterate_width)] for i in range(iterate_height)])


    def __pow__(self, other):
        if (self.width >= other.width) and (self.height >= other.height):
            return Grid2D([[self.grid[i][j] ** other.grid[i][j] for j in range(other.width)] for i in range(other.height)])            
        
        elif (self.width < other.width) and (self.height < other.height):
            return Grid2D([[self.grid[i][j] ** other.grid[i][j] for j in range(self.width)] for i in range(self.height)])


        else:
            iterate_width = self.width if self.width <= other.width else other.width
            iterate_height = self.height if self.height <= other.height else other.height
            return Grid2D([[self.grid[i][j] ** other.grid[i][j] for j in range(iterate_width)] for i in range(iterate_height)])
           

    def __eq__(self, other):
        if (self.width >= other.width) and (self.height >= other.height):
            return all([all([self.grid[i][j] == other.grid[i][j] for j in range(other.width)]) for i in range(other.height)])            
        
        elif (self.width < other.width) and (self.height < other.height):
            return all([all([self.grid[i][j] == other.grid[i][j] for j in range(self.width)]) for i in range(self.height)])


        else:
            iterate_width = self.width if self.width <= other.width else other.width
            iterate_height = self.height if self.height <= other.height else other.height
            return all([all([self.grid[i][j] == other.grid[i][j] for j in range(iterate_width)]) for i in range(iterate_height)])

    
    def __contains__(self, other):
        if other.width > self.width or other.height > self.height:
            return False
        
        for i in range(self.height - other.height + 1):
            for j in range(self.width - other.width + 1):
                sub_grid = [self.grid[o + i][j:j + other.width] for o in range(other.height)]
                if sub_grid == other.grid:
                    return True
        return False


# Základní testy:
grid1 = Grid2D([[1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [3, 4, 5, 6, 7],
                [4, 5, 6, 7, 8]])
grid2 = Grid2D([[1, 1, 1, 1, 1]])


assert grid1 + grid2 == Grid2D([[2, 3, 4, 5, 6]])
assert grid1 + grid2 == Grid2D([[2, 3, 4, 5, 6],
                                [2, 3, 4, 5, 6],
                                [3, 4, 5, 6, 7],
                                [4, 5, 6, 7, 8]])
assert grid1 ** grid1 == \
        Grid2D([[1, 4, 27, 256, 3125],
                [4, 27, 256, 3125, 46656],
                [27, 256, 3125, 46656, 823543],
                [256, 3125, 46656, 823543, 16777216]])

assert grid1 != grid2
assert grid1 == Grid2D([[1], [2], [3], [4], [5]])

assert Grid2D([[1, 2], [2, 3]]) in grid1
