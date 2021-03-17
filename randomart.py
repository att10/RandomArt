from PIL import Image
from PIL import ImageOps
import numpy as np
import random


side_length = 56

square = Image.open("square.png")
top_left = Image.open("corner.png")
bot_left = top_left.rotate(90)
bot_right = bot_left.rotate(90)
top_right = bot_right.rotate(90)

print(np.array(square))

original = Image.open("art.png")
output = Image.new("RGBA", (10*56, 10*56))
output_px = np.array(output)

shapes = [square, top_left, top_right, bot_right, bot_left]

def get_shape():
    return random.choice(shapes)

def make_art(grid_size):
    for i in range(0, grid_size):       #row
        for j in range(0, grid_size):   #col
            row = i*side_length
            col = j*side_length
            output_px[row:row+side_length, col:col+side_length] = np.array(get_shape())

def main():
    make_art(10)
    Image.fromarray(output_px).show()
    

if __name__ == "__main__":
    main()




