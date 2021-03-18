from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

import numpy as np
import random


side_length = 56

square = Image.open("square.png")
top_left = Image.open("corner2.png")
bot_left = top_left.rotate(90)
bot_right = bot_left.rotate(90)
top_right = bot_right.rotate(90)

original = Image.open("art.png")
output = Image.new("RGBA", (10*56, 10*56))
output_px = np.array(output)

red = [237, 28, 36, 255]
black = [0, 0, 0, 255]

shapes = [square, top_left, top_right, bot_right, bot_left]
colors = [[223, 226, 75, 255], [144, 176, 227, 255], [0, 0, 0, 255], 
        [28, 52, 38, 255],[215, 59, 21, 255],[36, 36, 72, 255], 
        [255, 137, 123, 255], [178, 86, 39, 255], [124, 26, 69, 255], 
        [254, 182, 39, 255], [255, 255, 255, 255], [183, 183, 183, 255], 
        [246,202,189, 255], [236,217,210, 255], [103,201,186, 255], [163,223,198,255]]

# Williams Identity Colors and Color Distribution
w_colors = [[80, 0, 130, 255], [255, 190, 10, 255], black, [255, 255, 255, 255],
[40, 0, 80, 255], [177, 0, 142, 255], [200, 105, 20, 255], [255, 120, 0, 255]]

w_weights = [22, 22, 7, 22, 7, 7, 7, 7]



def get_shape():
    return random.choice(shapes)

def get_color():
    return random.choice(colors)

def get_w_color():
    return random.choices(w_colors, weights=w_weights, k=1)[0]

def make_art(grid_size):
    for i in range(0, grid_size):       #row
        for j in range(0, grid_size):   #col
            row = i*side_length
            col = j*side_length
            output_px[row:row+side_length, col:col+side_length] = np.array(get_shape())
            color1 = get_w_color()
            color2 = get_w_color()
            for pi in range(row, row+side_length):
                for pj in range(col, col+side_length):
                    if np.array_equal(output_px[pi, pj], red):
                        output_px[pi, pj] = color1
                    elif np.array_equal(output_px[pi, pj], black):
                        output_px[pi, pj] = color2
                        
def main():
    make_art(10)
    Image.fromarray(output_px).show()
    #Image.fromarray(output_px).filter(ImageFilter.SMOOTH).show()
    

if __name__ == "__main__":
    main()




