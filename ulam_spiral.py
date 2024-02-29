#!/usr/bin/python3

from PIL import Image, ImageDraw
from math import sqrt

def prime_test(n):
    if n > 1:
        div_list = [1, n]
        for i in range(2, int(sqrt(n)+1)):
            if n%i == 0:
                div_list.append(i)
        if len(div_list) == 2:
            return True
        else:
            return False
    else:
        return False

print(prime_test(5))


# draw ulam spiral
square_size = 5
size = 500
img = Image.new(mode="RGB", size=(size*square_size, size*square_size), color="white")
draw = ImageDraw.Draw(img)

# create spiral
square_num = size * size
point = [0, 0]
counter = 1
iteration = 0

for k in range(square_num):
    if counter < square_num+1:
        if 2*k == iteration:
            iteration = 0
            k += 1

            for j in range(2):
                for _ in range(k):
                    # draw points
                    if prime_test(counter) and counter == 2:
                        draw.rectangle([(point[0] + size/2) * square_size + 0.5,
                                        (point[1] * -1 + size/2) * square_size + 0.5,
                                        (point[0] + size/2) * square_size + square_size - 0.5, 
                                        (point[1] * -1 + size/2) * square_size + square_size - 0.5],
                                        fill="red")
                    # draw first point red
                    elif prime_test(counter):
                        draw.rectangle([(point[0] + size/2) * square_size + 0.5,
                                        (point[1] * -1 + size/2) * square_size + 0.5,
                                        (point[0] + size/2) * square_size + square_size - 0.5, 
                                        (point[1] * -1 + size/2) * square_size + square_size - 0.5],
                                        fill="black")

                    if k % 2 == 0:
                        point[j] -= 1
                    else:
                        point[j] += 1
                    iteration += 1
                    counter += 1
    else:
        break

img.save('spiral.png')

