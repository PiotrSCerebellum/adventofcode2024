def make_grid(data:str):
    grid=data.splitlines()
    return grid
def grid_search(grid:list[str]):
    total=0
    total_old=0
    for vertical in range(len(grid)):
        for horizontal in range(len(grid[0])):
            if grid[vertical][horizontal]=='X':
                total_old+=check_xmas(grid,horizontal,vertical)
            if grid[vertical][horizontal]=='A':
                total+=check_shapes(grid,horizontal,vertical)

    return total,total_old

def safe_access(grid, row, col):
    default=''
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    return default

def check_shapes(grid:list[str],horizontal:int,vertical:int)->int:
    a = safe_access(grid, vertical - 1, horizontal - 1)
    a += "A"
    a += safe_access(grid, vertical + 1, horizontal + 1)
    b = safe_access(grid, vertical - 1, horizontal + 1)
    b += "A"
    b += safe_access(grid, vertical + 1, horizontal - 1)
    if a!='MAS' and a!='SAM':
        return 0
    if b!='MAS' and b!='SAM':
        return 0
    return 1



# part one
def check_xmas(grid: list[str], horizontal: int, vertical: int)->int:
    num_of_xmas=0
    directions={ 'up':'','down':'','left':'','right':'','left_up':'','right_up':'','left_down':'','right_down':''}
    directions['left'] = ''.join(safe_access(grid, vertical, horizontal - i) for i in range(4))
    directions['right'] = ''.join(safe_access(grid, vertical, horizontal + i) for i in range(4))
    for i in range(4):
        directions['up'] += safe_access(grid, vertical - i, horizontal)
        directions['down'] += safe_access(grid, vertical + i, horizontal)
        directions['left_up'] += safe_access(grid, vertical - i, horizontal - i)
        directions['right_up'] += safe_access(grid, vertical - i, horizontal + i)
        directions['left_down'] += safe_access(grid, vertical + i, horizontal - i)
        directions['right_down'] += safe_access(grid, vertical + i, horizontal + i)
    for direction in directions:
        if directions[direction]=='XMAS':
            num_of_xmas+=1
    return num_of_xmas


with open(r".\\data\\day4.txt", "r") as file:
    data=file.read()
grid=make_grid(data)
total,total_old=grid_search(grid)
print(f"Total occurances of shapes:{total}, and xmas:{total_old}")




