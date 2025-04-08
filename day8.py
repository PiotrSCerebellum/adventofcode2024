
def find_antenas(antena_map:list):
    antena_repository={}
    antena_types=set()
    for x,y in [(x,y) for x in range(len(antena_map[0])) for y in range(len(antena_map))]:
        if antena_map[y][x]!='.':
            if antena_map[y][x] not in antena_types:
                antena_types.add(antena_map[y][x])
                antena_repository.update({antena_map[y][x]:[(x,y)]})
            else:
                antena_repository[antena_map[y][x]].append((x,y))
    return antena_repository,antena_types
def find_antipodes(antena_list:list):
    antipodes=set()
    while len(antena_list)>1:
        x,y=antena_list.pop()
        for x1,y1 in antena_list:
            distance_y=(y-y1)
            distance_x=(x-x1)
            anti=[(x+distance_x,y+distance_y),(x1-distance_x,y1-distance_y)]
            for a in anti:
                if not outside(a[0],a[1]):
                    antipodes.add(a)
    return antipodes
def outside(x,y):
    return not (0<=x<width and 0<=y<height)
def find_antipodes_part2(antena_list:list):
    antipodes=set()
    while len(antena_list)>1:
        x,y=antena_list.pop()
        for x1,y1 in antena_list:
            distance_y=(y-y1)
            distance_x=(x-x1)
            anti=[]
            xa,ya=x,y
            while not outside(xa,ya):
                anti.append((xa,ya))
                xa,ya=(xa+distance_x,ya+distance_y)
            xa,ya=x1,y1
            while not outside(xa,ya):
                anti.append((xa,ya))
                xa,ya=(xa-distance_x,ya-distance_y)
            for a in anti:
                if not outside(a[0],a[1]):
                    antipodes.add(a)
    return antipodes


with open(r".\\data\\day8.txt", "r") as file:
    antena_map = [[col for col in line.strip()] for line in file]
width=len(antena_map[0])
height=len(antena_map)
antena_repository,antena_types=find_antenas(antena_map)
antipodes=[]
antipodes_part2=[]
for antena_type in antena_types:
    # antipodes+=([*find_antipodes(antena_repository[antena_type])])
    antipodes_part2+=([*find_antipodes_part2(antena_repository[antena_type])])
print(f"Total antipodes: {len(set(antipodes))} ")
print(f"With harmonics: {len(set(antipodes_part2))}")
# with open(r".\\data\\day8_solve.txt", "w") as file:
#     for x,y in antipodes:
#         antena_map[y][x]='#'
#     buffer='\n'.join(''.join(inner_list) for inner_list in antena_map)
#     file.writelines(buffer)
