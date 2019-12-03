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

