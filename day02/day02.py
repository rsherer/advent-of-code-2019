'''
intcodes and opcodes

intcode = position 0 will be a one. Take the numbers at position 1 and position
2, add them together, then store this value at the number in position 3.

opcode = position 0 will be a two. The process is the same thereafter as an
intcode, except multiply the numbers in stead of adding.
'''

import numpy as np 
from typing import List, Tuple

def intcode(codes: List[int]) -> Tuple[int, int]:
    total = sum(codes[1:3])
    return (total, codes[3])

def opcode(codes: List[int]) -> Tuple[int, int]:
    total = codes[1] * codes[2]
    return (total, codes[3])

import csv

with open('input.txt') as f:
    program = csv.reader(f)
    codes = [code for code in program][0]
    codes = [int(code) for code in codes]

print(codes)