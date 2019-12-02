'''
Part 1: intcodes and opcodes

intcode = position 0 will be a one. Take the numbers at position 1 and position
2, add them together, then store this value at the number in position 3.

opcode = position 0 will be a two. The process is the same thereafter as an
intcode, except multiply the numbers in stead of adding.
'''

import numpy as np 
from typing import List, Tuple

def add_num(n1: int, n2: int) -> int:
    return n1 + n2

def mult_num(n1: int, n2: int) -> int:
    return n1 * n2

def intcode(prog: List[int]) -> List[int]:
    idx = 0

    while prog[idx] != 99:
        if prog[idx] == 1:
            p1 = prog[idx + 1]
            p2 = prog[idx + 2]
            placement = prog[idx + 3]
            prog[placement] = add_num(prog[p1], prog[p2])
        elif prog[idx] == 2:
            p1 = prog[idx + 1]
            p2 = prog[idx + 2]
            placement = prog[idx + 3]
            prog[placement] = mult_num(prog[p1], prog[p2])
        else:
            raise ValueError(f"incorrect opcode: {INPUTTEXT[idx]}")

        idx += 4
    
    return prog

INPUTTEXT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
INPUTTEXT[1] = 12
INPUTTEXT[2] = 2

# import csv

# with open('input.txt') as f:
#     program = csv.reader(f)
#     raw = [code for code in program][0]
#     program = [int(code) for code in raw]

assert intcode([1, 0, 0, 0, 99]) == [2,0,0,0,99], f"{intcode([1, 0, 0, 0, 99])}"
assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

print(intcode(INPUTTEXT))

'''
Part 2:

To complete the gravity assist, you need to determine what pair of inputs 
produces the output 19690720."

The inputs should still be provided to the program by replacing the values at 
addresses 1 and 2, just like before. In this program, the value placed in 
address 1 is called the noun, and the value placed in address 2 is called the 
verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just 
like before. Each time you try a pair of inputs, make sure you first reset the 
computer's memory to the values in the program (your puzzle input) - in other 
words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 
19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the 
answer would be 1202.)
'''

P2TEXT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
