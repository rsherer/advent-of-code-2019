'''
Part 1

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to 
find the fuel required for a module, take its mass, divide by three, round 
down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel 
required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, 
individually calculate the fuel needed for the mass of each module (your puzzle 
input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your 
spacecraft?
'''

import numpy as np

def fuel_requirment(mass: int) -> int:
    return mass // 3 - 2

assert fuel_requirment(12) == 2
assert fuel_requirment(14) == 2
assert fuel_requirment(1969) == 654
assert fuel_requirment(100756) == 33583

with open('input.txt') as f:
    module_masses = [int(line.strip()) for line in f]
    fuel_sum = sum(fuel_requirment(mass) for mass in module_masses)

print(fuel_sum)