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
from typing import List, NamedTuple, Tuple, Dict
import math
from itertools import permutations

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

def get_points(belt: List[str]) -> List[Point]:
    points = []
    x = y = 0
    for iy, row in enumerate(belt):
        for ix, ast in enumerate(row):
            if ast == '#':
                points.append(Point(ix, iy))
    return points

test_asteroids = get_points(test_belt)
#print(test_asteroids)

def get_slope(p1: Point, p2: Point) -> float:
    if p1.x - p2.x == 0:
        return math.inf
    else:
        return round((p1.y - p2.y)/(p1.x - p2.x), 4)

p1 = Point(1, 0)
p2 = Point(4, 0)
p3 = Point(1, 4)

assert get_slope(p1, p2) == 0
assert get_slope(p1, p3) == math.inf
assert get_slope(p2, p3) == -1.3333

def get_distance(p1: Point, p2: Point) -> float:
    # distance is positive if vector goes up, negative if vector goes down
    # vector that goes right is positive, left is negative
    if p1.x == p2.x:
        return (p1.y - p2.y)
    if p1.y == p2.y:
        return (p2.x - p1.x)
    if p1.y > p2.y:
        return math.sqrt((p1.x - p2.x)**2 +(p1.y - p2.y)**2)
    else:
        return -math.sqrt((p1.x - p2.x)**2 +(p1.y - p2.y)**2)

assert get_distance(p1, p2) == 3
assert get_distance(p1, p3) == -4
assert get_distance(p2, p3) == -5

# now go through all the asteroids, and find the distance and slopes from 
# each asteroid to the others. shortest distance with the same slope counts as 
# being since. else it's blocked

def get_number_detected(belt: List[Point]) -> Dict[Point, Tuple[float, str]]:
    detected = {ast: set() for ast in belt}

    for ast1, ast2 in permutations(belt, 2):
        #print(ast1, ast2)
        slope = get_slope(ast1, ast2)
        dist = get_distance(ast1, ast2)
        sign = 'pos' if dist > 0 else 'neg'
        #print(f"{ast1} to {ast2} has slope {slope} and distance {dist} and sign {sign}")
        if (slope, sign) not in detected[ast1]:
            detected[ast1].add((slope, sign))

    return {k: len(v) for k, v in detected.items()}

test_num_detected = get_number_detected(test_asteroids)
print(max(test_num_detected, key=test_num_detected.get))
print(test_num_detected[max(test_num_detected, key=test_num_detected.get)])

# assert len(test_num_detected[Point(1, 0)]) == 7
# assert len(test_num_detected[Point(0, 2)]) == 6
# assert len(test_num_detected[Point(4, 2)]) == 5
# assert len(test_num_detected[Point(3, 4)]) == 8

asteroids = get_points(asteroid_belt)
num_detected = get_number_detected(asteroids)
print(max(num_detected, key=num_detected.get))
print(num_detected[max(num_detected, key=num_detected.get)])

#answer is asteroid at Point(26, 36) can detect 347 other asteroids

"""Part 2
"""



