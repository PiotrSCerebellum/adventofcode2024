from enum import Enum
import itertools

class Guard:
    loops=set()
    traversed=set()
    class Direction(Enum):
        UP = lambda x, y: (x, y - 1)
        RIGHT = lambda x, y: (x + 1, y)
        DOWN = lambda x, y: (x, y + 1)
        LEFT = lambda x, y: (x - 1, y)
    DIRECTIONS = [(Direction.UP,'^'), (Direction.RIGHT,'>'), (Direction.DOWN,'v'), (Direction.LEFT,'<')]
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        for d in self.DIRECTIONS:
            if d[1]==direction:
                self.direction = d  
                break
        self.direction_cycle = itertools.cycle(self.DIRECTIONS)
        while next(self.direction_cycle) != self.direction:
            pass
    def look_for_loops(self,map:list):
        result=Shadow(self.x,self.y,self.direction[1]).march(map,self.traversed)
        return result
    def march(self, map: list[list[list]]):
        print(self.x,self.y)
        self.traversed.add((self.x,self.y,self.direction[1]))
        new_x, new_y = self.direction[0](self.x, self.y)

        if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
            map[self.y][self.x].append(self.direction[1])
            return False
        if "#" in map[new_y][new_x]:
            self.direction = next(self.direction_cycle)
            return True
        else:
            loop=self.look_for_loops(map)
            if loop[0]:
                loop=frozenset(loop[1])
                self.loops.add(loop)
            map[self.y][self.x].append(self.direction[1])
            
            self.x, self.y = new_x, new_y
            return True
class Shadow(Guard):
    visited=[]
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.x=x
        self.y=y
        self.visited=[(x,y,direction)]
    def march(self, map, traversed):
        self.direction = next(self.direction_cycle)
        while True:
            new_x, new_y = self.direction[0](self.x, self.y)
            if (new_x,new_y,self.direction[1]) in traversed:
                return False,self.visited
            if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
                return False,self.visited
            if (new_x,new_y,self.direction[1]) in self.visited:
                    return True,self.visited
            elif "#" in map[new_y][new_x]:
                self.direction = next(self.direction_cycle)
            else:
                self.x, self.y = new_x, new_y
                self.visited.append((self.x,self.y,self.direction[1]))


def read_map(data:str):
    map=[]
    for line in data.splitlines():
        chars=[ [x] for x in line]
        map.append((chars))
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col][0] in '<>v^':
                match map[row][col][0]:
                    case '<':
                        return map,Guard(col,row,('<'))
                    case '>':
                        return map,Guard(col,row,('>'))
                    case '^':
                        return map,Guard(col,row,('^'))
                    case 'V':
                        return map,Guard(col,row,('v'))
                    case _:
                        print('Bad data')
def explore_map(map:list[list],guard:Guard):
    exploring=True
    while exploring:
        exploring=guard.march(map)
    return count_x(map)
def count_x(map):
    total=0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if not set(map[row][col]).isdisjoint(set('<>v^')):
                total+=1
    return total



with open(r".\\data\\day6.txt", "r") as file:
    data=file.read()
map,guard=read_map(data)
total=explore_map(map,guard)
print(f"Total traversed tiles:{total}, found {len(guard.loops)} loops")
# with open(r".\\data\\day6_small_traversal.txt", "w") as file:
#     buffer='\n'.join(''.join(inner_list[0]) for inner_list in map)
#     file.writelines(buffer)

