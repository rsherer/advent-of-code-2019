'''
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


def is_double(pwd: str) -> bool:
    for c1, c2 in zip(pwd, pwd[1:]):
        if c1 == c2:
            return True
    return False

assert is_double('111111') == True
assert is_double('223450') == True
assert is_double('123789') == False

def is_increasing(pwd: str) -> bool:
    for c1, c2 in zip(pwd, pwd[1:]):
        if c1 > c2:
            return False
    return True

assert is_increasing('111111') == True
assert is_increasing('223450') == False
assert is_increasing('123789') == True

def check_password(pwd: int) -> bool:
    if is_double(str(pwd)) and is_increasing(str(pwd)):
        return True
    return False  

assert check_password('111111') == True
assert check_password('223450') == False
assert check_password('123789') == False   
    
print(sum(check_password(pwd) for pwd in range(372304, 847061)))



