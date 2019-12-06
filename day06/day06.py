"""
Part 1: orbits and indirect orbits

Whenever A orbits B and B orbits C, then A indirectly orbits C. 
This chain can be any number of objects long: if A orbits B, B orbits C, and 
C orbits D, then A indirectly orbits D.

Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the 
one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 
7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
"""

from typing import List, Tuple, Dict, DefaultDict
from collections import defaultdict

def parse_orbit_map(orbit_map: str) -> Tuple[str, str]:
    'ob1 has ob2 orbiting it'
    ob1, ob2 = '', ''
    for i, char in enumerate(orbit_map):
        if char != ')':
            ob1 += char
        else:
            ob2 = orbit_map[i + 1:]
            break
    return ob1, ob2

#print(parse_orbit_map('J1C)J1M'))

#test on first three entries from input
# assert parse_orbit_map('J1C)J1M') == {'J1C': 'J1M'}
# assert parse_orbit_map('N2W)2DM') == {'N2W': '2DM'}
# assert parse_orbit_map('DST)VZL') == {'DST': 'VZL'}


# convert oject maps to dictionary of dictionaries
with open('input.txt') as f:
    mappings = f.readlines()
    orbit_maps = [parse_orbit_map(mapping.strip('\n')) for mapping in mappings]
    
#print(orbit_maps)

def find_com(orbit_map: List[Tuple[str, str]], root) -> int:
    for i, orbits in enumerate(orbit_map):
        if orbits[0] == root:
            return i
    raise RuntimeError(f"there is no {root} in the orbit map")

def build_orbit_tree(orbit_map: List[Tuple[str, str]]) -> DefaultDict[str, List[str]]:
    tree: DefaultDict[str, List[str]] = defaultdict(list)
    for k, v in orbit_map:
        tree[k].append(v)
    return tree
    
def count_steps(orbit_map: List[Tuple[str, str]], root: str='COM') -> int:
    pass

#    while True:

print(build_orbit_tree(orbit_maps))