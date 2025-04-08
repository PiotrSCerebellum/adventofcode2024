

with open(r".\\data\\day6.txt", "r") as file:
    grid = [[col for col in line.strip()] for line in file]
width, height = (len(grid[0]), len(grid))
def outside(x,y):
    return not (0<=x<width and 0<=y<height)
directions = [(0,-1), (1,0), (0,1), (-1,0)]
neighbor_map = dict()
obstacles = set()
nodes = [(x, y, d) for x in range(width) for y in range(height) for d in range(4)]

for x,y in [(x,y) for x in range(width) for y in range(height)]:
    if grid[y][x] == "#":
        obstacles.add((x,y))
    elif grid[y][x] == "^":
        startpos = (x,y,0)
for x,y,d in nodes:
    if outside(x+directions[d][0], y+directions[d][1]):
        neighbor_map[(x,y,d)] = (-1,-1,-1)
    elif (x+directions[d][0], y+directions[d][1]) in obstacles:
        neighbor_map[(x,y,d)] = (x,y,(d+1)%4)
    else:
        neighbor_map[(x,y,d)] = (x+directions[d][0], y+directions[d][1], d)

main_path = []
original_visited = set()
position = startpos

while not position==(-1,-1,-1):
    main_path.append(position)
    original_visited.add((position[0],position[1]))
    position = neighbor_map[position]

loop_obstacles = set()
non_loop_obstacles = set()
for index, position in enumerate(main_path[1:],1):
    x,y = (position[0],position[1])
    if (x,y) in loop_obstacles or (x,y) in non_loop_obstacles:
        continue
    for d in range(4):
        previous = (x-directions[d][0], y-directions[d][1], d)
        neighbor_map[previous] = (previous[0], previous[1], (d+1)%4)
    visited = set()
    cur = main_path[index-1]
    while not cur==(-1,-1,-1) and cur not in visited:
        visited.add(cur)
        cur = neighbor_map[cur]
    if cur==(-1,-1,-1):
        non_loop_obstacles.add((position[0],position[1]))
    else:
        loop_obstacles.add((position[0],position[1]))
    for d in range(4):
        previous = (x-directions[d][0], y-directions[d][1], d)
        neighbor_map[previous] = (position[0],position[1],d)


print(f"{len(loop_obstacles)} obstacles lead to a loop. {len(non_loop_obstacles)} don't. {len(loop_obstacles)+len(non_loop_obstacles)} positions investigated")