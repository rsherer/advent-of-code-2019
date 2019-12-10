"""
Day 10 of advent of code, 2019. 

Part 1. Find the position with the most number of visible asteroids.

The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).

Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.

For example, consider the following map:

.#..#
.....
#####
....#
...##

The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:

.7..7
.....
67775
....7
...87

"""
from typing import List, NamedTuple, Tuple
import math

with open('input.txt') as f:
    asteroid_belt = [row.strip('\n') for row in f.readlines()]

example_belt = """.#..#
.....
#####
....#
...##
"""
test_belt = example_belt.split('\n')

def get_asteroid_belt_width(belt: List[str]) -> int:
    return len(belt[0])

assert get_asteroid_belt_width(asteroid_belt) == 42
assert get_asteroid_belt_width(test_belt) == 5

class Point(NamedTuple):
    x: int
    y: int

def asteroid_slope(p1: Point, p2: Point) -> float:
    if p1.x - p2.x == 0:
        return math.inf
    else:
        return (p1.y - p2.y)/(p1.x - p2.x)

p1 = Point(1, 0)
p2 = Point(4, 0)
p3 = Point(1, 4)

assert asteroid_slope(p1, p2) == 0
assert asteroid_slope(p1, p3) == math.inf
assert asteroid_slope(p2, p3) == -4/3

def get_points(belt: List[str]) -> List[Point]:
    points = []
    x = y = 0
    for iy, row in enumerate(belt):
        for ix, ast in enumerate(row):
            if ast == '#':
                points.append(Point(ix, iy))
    return points

test_asteroids = get_points(test_belt)
print(test_asteroids)

def get_distance(p1: Point, p2: Point) -> float:
    if p1.x == p2.x:
        return abs(p1.y - p2.y)
    if p1.y == p2.y:
        return abs(p1.x - p2.x)
    return math.sqrt((p1.x - p2.x)**2 +(p1.y - p2.y)**2)

assert get_distance(p1, p2) == 3
assert get_distance(p1, p3) == 4
assert get_distance(p2, p3) == 5

