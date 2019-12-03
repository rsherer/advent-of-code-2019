'''
Day 3, part 1

Find the manhattan distance where the wires cross each other, closest to the 
central port.

Manhattan distance is the x-distance plus the y-distance.
'''

from typing import NamedTuple, List, Set

class Coord(NamedTuple):
    x: int
    y: int

def where_traveled(path: str) -> Set[Coord]:
    x = 0
    y = 0

    coordinates = set()

    for wire in path.split(','):
        direction = wire[0]
        length = int(wire[1:])

        for point in range(length):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            coordinates.add(Coord(x, y))
    return coordinates

def cross_paths(path1: str, path2: str) -> Set[Coord]:
    points1 = where_traveled(path1)
    points2 = where_traveled(path2)
    return points1.intersection(points2)

def manhattan_distance(coord: Set[Coord]) -> int:
    return abs(coord.x) + abs(coord.y)

def closest_crossed_wire(p1: str, p2: str) -> int:
    crosses = cross_paths(p1, p2)
    return min([manhattan_distance(cross) for cross in crosses])

with open('input.txt') as f:
    p1, p2 = f.readlines()
    PATH1 = p1.strip('\n')
    PATH2 = p2

print(closest_crossed_wire(PATH1, PATH2))



'''Day 3, part 2

In the above example, the intersection closest to the central port is reached 
after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second 
wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 
8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 
steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
'''


