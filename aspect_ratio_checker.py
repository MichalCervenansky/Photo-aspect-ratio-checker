import os
import sys

from PIL import Image

# Check number of command line arguments
if len(sys.argv) != 2:
    raise RuntimeError("Use with correct directory path in first argument")

# Use directory from first command line argument
dirname = sys.argv[1]

# Aspect ratio 3:2, change it to 4:3 or something else if you need to.
longEdge = 3
shortEdge = 2
# Iterator to count number of photos with correct aspect ratio.
correct = 0

for filename in os.listdir(dirname):
    if filename[-4:].lower() == ".jpg":
        image = Image.open(dirname + os.sep + filename)
        width, height = image.size
        # Because of possible landscape and portrait orientation of image
        if not (width // longEdge == height // shortEdge or width // shortEdge == height // longEdge):
            print(filename + " (" + str(width) + ":" + str(height) + ")")
        else:
            correct += 1
print(str(correct) + " of " + str(len(os.listdir(dirname))) + " files have correct aspect ratio.")
