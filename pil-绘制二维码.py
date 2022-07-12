import itertools
from PIL import Image


max = 200
file = open("./flag/qr.txt", "r")

img = Image.new("RGB", (max, max))
for y, x in itertools.product(range(max), range(max)):
    pixel = eval(file.readline())
    img.putpixel([x, y], pixel)

img.show()