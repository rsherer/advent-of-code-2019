"""
Day 8

Images are sent as a series of digits that each represent the color of a single 
pixel. The digits fill each row of the image left-to-right, then move downward 
to the next row, filling rows top-to-bottom until every pixel of the image is 
filled.

Each image actually consists of a series of identically-sized layers that are 
filled in this way. So, the first digit corresponds to the top-left pixel of 
the first layer, the second digit corresponds to the pixel to the right of that 
on the same layer, and so on until the last digit, which corresponds to the 
bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 
123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would 
like you to find the layer that contains the fewest 0 digits. On that layer, 
what is the number of 1 digits multiplied by the number of 2 digits?
"""

import numpy as np
from collections import Counter
from typing import List

with open('input.txt') as f:
    codes = [int(char) for char in f.read()]
    #print(codes)
    #print(len(codes))

test_codes = [1,2,3,4,5,6,7,8,9,0,1,2]    

def get_image_layers(series: str, wide: int, tall: int) -> List[List[int]]:
    layer = wide * tall
    num_layers = len(series) // layer
    layers = []
    for n in range(num_layers):
        # print(f"layer {n} is {layer} digits long")
        # print(f"the start of the series is {series[(n * layer)]}")
        # print(f"the end of hte series is {(n * 1 + layer)}")
        layers.append(series[(n * layer):((n + 1) * layer)])
    return layers

layers = get_image_layers(codes, 25, 6)
#print(layers)

zeros = 150
idx = 0
for i, layer in enumerate(layers):
    cnt = Counter(layer)
    if cnt[0] < zeros:
        min_zero = cnt[0]
        zeros = min_zero
        idx = i
print(f"layer is {idx}")
