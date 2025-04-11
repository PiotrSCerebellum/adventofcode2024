def make_connections(grid:list[list]):
    adjecent={}
    starting_points=[]
    for x,y in [(x,y) for x in range(width) for y in range(height)]:
        adjecent.update(check_adjecency(x,y,grid))
        if grid[y][x]==0:
            starting_points.append((x,y))
    return adjecent,starting_points
def outside(x,y):
    if 0>x or x>=width or 0>y or y>=height:
        return True
    else:
        return False
def check_adjecency(x,y,grid:list[list]):
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    adjecent={(x,y):[]}
    for d in directions:
        x1,y1=add_points((x,y),d)
        if outside(x1,y1):
            continue
        if grid[y][x]-grid[y1][x1]==-1:
            adjecent[(x,y)].append((x1,y1))
    return adjecent     
def dfs_recursive(graph, start_node, visited=None):
    if visited is None:
        visited = set()  
    visited.add(start_node)   
    for neighbour in graph[start_node]:  
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)

def all_paths_bfs(graph, start_node,grid): 
    queue = []
    paths=0
    queue.append(start_node)
    while queue:          
        m = queue.pop(0) 
        if grid[m[1]][m[0]]==9:
            paths+=1
        for neighbour in graph[m]:
                queue.append(neighbour)
    return paths

def add_points(tuple1:tuple,tuple2:tuple):
    return (tuple1[0]+tuple2[0],tuple1[1]+tuple2[1])
with open(r".\\data\\day10.txt", "r") as file:
    grid=[[int(col) for col in line.strip()] for line in file]
height=len(grid)
width=len(grid[0])
adjecent,starting=make_connections(grid)
total=0
for point in starting:
    total+=all_paths_bfs(adjecent,point,grid)
print(f"Total points:{total}")
