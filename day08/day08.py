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

def get_pixel_layers(series: List[int], wide: int, tall: int) -> List[List[int]]:
    layer = wide * tall
    num_layers = len(series) // layer
    layers = []
    for n in range(num_layers):
        # print(f"layer {n} is {layer} digits long")
        # print(f"the start of the series is {series[(n * layer)]}")
        # print(f"the end of hte series is {(n * 1 + layer)}")
        layers.append(series[(n * layer):((n + 1) * layer)])
    return layers

layers = get_pixel_layers(codes, 25, 6)
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

#answer
print(layers[5].count(1) * layers[5].count(2))


"""
part 2

Now you're ready to decode the image. The image is rendered by stacking the 
layers and aligning the pixels with the same positions in each layer. The 
digits indicate the color of the corresponding pixel: 0 is black, 1 is white, 
and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in 
back. So, if a given position has a transparent pixel in the first and second 
layers, a black pixel in the third layer, and a white pixel in the fourth 
layer, the final image would have a black pixel at that position.

or example, given an image 2 pixels wide and 2 pixels tall, the image data 
0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in 
each position:

-The top-left pixel is black because the top layer is 0.
-The top-right pixel is white because the top layer is 2 (transparent), but the 
second layer is 1.
-The bottom-left pixel is white because the top two layers are 2, but the third 
layer is 1.
-The bottom-right pixel is black because the only visible pixel in that position 
is 0 (from layer 4).
-So, the final image looks like this:

01
10
What message is produced after decoding your image?
"""

def get_image(series: List[int], wide: int, tall: int) -> List[int]:
     # 0 is black, 1 is white, and 2 is transparent.
    message = [2 for elem in range(wide * tall)]
    layers = get_pixel_layers(series, 25, 6)
    for layer in layers:
        for i, digit in enumerate(layer):
            if message[i] == 2:
                message[i] = digit
    for n in range(tall):
        print(message[(n * wide):((n + 1) * wide)])

print(get_image(codes, 25, 6))