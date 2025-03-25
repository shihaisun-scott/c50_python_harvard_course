import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=[images[1]], duration = 200, loop = 0)

# then do the following to create a gif
# python costumes.py costumes1.gif costimes2.gif
# code costimes.gif