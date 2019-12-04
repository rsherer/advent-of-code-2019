'''
Part 1

--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a 
password. The Elves had written the password on a sticky note, but someone 
threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or 
stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet 
these criteria?

Your puzzle input is 372304-847060.
'''

from collections import Counter

def is_double(pwd: str) -> bool:
    for c1, c2 in zip(pwd, pwd[1:]):
        if c1 == c2:
            return True
    return False

assert is_double('111111')
assert is_double('223450')
assert not is_double('123789')

def is_increasing(pwd: str) -> bool:
    for c1, c2 in zip(pwd, pwd[1:]):
        if c1 > c2:
            return False
    return True

assert is_increasing('111111')
assert not is_increasing('223450')
assert is_increasing('123789')

def check_password(pwd: int) -> bool:
    if is_double(str(pwd)) and is_increasing(str(pwd)):
        return True
    return False  

assert check_password('111111')
assert not check_password('223450')
assert not check_password('123789')

START = 372304
END = 847060

print(sum(check_password(pwd) for pwd in range(START, END + 1)))


'''
Part 2

An Elf just remembered one more important detail: the two adjacent matching 
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the 
following are now true:

112233 meets these criteria because the digits never decrease and all repeated 
digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group 
of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still 
contains a double 22).
How many different passwords within the range given in your puzzle input meet 
all of the criteria?

Your puzzle input is still 372304-847060.
'''

# def is_group(pwd: str) -> bool:
#     for c1, c2, c3 in zip(pwd, pwd[1:], pwd[2:]):
#         if c1 == c2 == c3:
#             return True
#     return False

def has_group_of_two(pwd: str) -> bool:
    count = Counter(pwd)
    for val in count.values():
        if val == 2:
            return True
    return False

assert has_group_of_two('112334')
assert not has_group_of_two('123444')
assert has_group_of_two('111122')

# assert not is_group('112233')
# assert is_group('123444')
# assert is_group('111122')


def check_password_partII(pwd: int) -> bool:
    if is_increasing(str(pwd)) and has_group_of_two(str(pwd)):
        return True
    return False
    
assert check_password_partII('112233') == True    
assert check_password_partII('123444') == False, f"{check_password_partII('123444')}"
assert check_password_partII('111122') == True

print(sum(check_password_partII(pwd) for pwd in range(START, END + 1)))

