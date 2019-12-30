"""
Day 22, part 1, a card shuffler

https://adventofcode.com/2019/day/22
"""

from typing import List

def new_stack(deck: List[int]) -> List[int]:
    return [num for num in reversed(deck)]

def cut(deck: List[int], n: int) -> List[int]:
    return deck[n:] + deck[:n]

deck = [num for num in range(10)]

assert new_stack(deck) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert cut(deck, 3) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
assert cut(deck, -4) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

def increment(deck: List[int], n: int) -> List[int]:
    shuffled = [0 for _ in range(len(deck))]
    for i, card in enumerate(deck):
        shuffled[(i * n) % len(deck)] = deck[i]
    return shuffled

assert increment(deck, 3) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

test1 = '''
deal with increment 7
deal with increment 9
cut -2
'''

test2 = '''
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
'''

print(deck)
for line in test2.split('\n'):
    #line = line.strip()
    if line == 'deal into new stack':
        deck = new_stack(deck)
    elif line.startswith('deal with'):
        number = int(line.split()[-1])
        deck = increment(deck, number)
    elif line.startswith('cut'):
        number = int(line.split()[-1])
        deck = cut(deck, number)
print(deck)

factory_deck = [num for num in range(10007)]

with open('input.txt') as f:
    new = cutting = inc = 0
    for line in f:
        #line = line.strip()
        if line.startswith('deal into'):
            factory_deck = new_stack(factory_deck)
            new += 1
        elif line.startswith('deal with'):
            number = int(line.split()[-1])
            factory_deck = increment(factory_deck, number)
            inc += 1
        elif line.startswith('cut'):
            number = int(line.split()[-1])
            factory_deck = cut(factory_deck, number)
            cutting += 1

print(new, cutting, inc)
print(factory_deck.index(2019))
print(factory_deck[2430])