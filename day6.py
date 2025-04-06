from enum import Enum
import itertools
class Direction(Enum):
    UP = lambda x, y: (x, y - 1)
    RIGHT = lambda x, y: (x + 1, y)
    DOWN = lambda x, y: (x, y + 1)
    LEFT = lambda x, y: (x - 1, y)
DIRECTIONS = [(Direction.UP,'^'), (Direction.RIGHT,'>'), (Direction.DOWN,'v'), (Direction.LEFT,'<')]
class Guard:
    loops=0
    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction  
        self.direction_cycle = itertools.cycle(DIRECTIONS)
        while next(self.direction_cycle) != direction:
            pass
    def look_for_loops(self,map:list,new_x,new_y):
        new_direction=next(self.direction_cycle)
        bounce_x, bounce_y = new_direction[0](new_x,new_y)
        while next(self.direction_cycle) != self.direction:
            pass
        try:
            if map[bounce_y][bounce_x] == new_direction[1]:
                new_x, new_y = self.direction[0](self.x, self.y)
                map[new_y][new_x] ='O' 
                return 1
        except IndexError:
            return 0
        return 0
    def march(self, map: list):
        new_x, new_y = self.direction[0](self.x, self.y)
        self.loops+=self.look_for_loops(map,new_x, new_y)
        if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
            map[self.y][self.x]=self.direction[1]
            return False
        if map[new_y][new_x] == "#":
            self.direction = next(self.direction_cycle)
            return True
        else:
            map[self.y][self.x]=self.direction[1]
            self.x, self.y = new_x, new_y
            return True


def read_map(data:str):
    map=[]
    for line in data.splitlines():
        map.append(list(line))
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] in '<>v^':
                match map[row][col]:
                    case '<':
                        return map,Guard(col,row,(Direction.LEFT,'<'))
                    case '>':
                        return map,Guard(col,row,(Direction.RIGHT,'>'))
                    case '^':
                        return map,Guard(col,row,(Direction.UP,'^'))
                    case 'V':
                        return map,Guard(col,row,(Direction.DOWN,'v'))
                    case _:
                        print('Bad data')
def explore_map(map:list[list[str]],guard:Guard):
    exploring=True
    while exploring:
        exploring=guard.march(map)
    return count_x(map)
def count_x(map):
    total=0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] in '<>v^':
                total+=1
    return total



with open(r".\\data\\day6_small.txt", "r") as file:
    data=file.read()
map,guard=read_map(data)
total=explore_map(map,guard)
print(f"Total traversed tiles:{total}, found {guard.loops} loops")
with open(r".\\data\\day6_small_traversal.txt", "w") as file:
    buffer='\n'.join(''.join(inner_list) for inner_list in map)
    file.writelines(buffer)

