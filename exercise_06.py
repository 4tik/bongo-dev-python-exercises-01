# Write a function named 
# “isLandscape” that takes 2 numbers (image width and height) as arguments 
# and the function returns Landscape if the image width has a higher value than height.
# Returns Portrait otherwise
# Hints: Use condition inside the function

def isLandscape(image_width=0, image_height=0):
    return "Landscape" if image_width>image_height else "Portrait"

image_width=100
image_height=20

print(f"image dimension: {isLandscape(image_width, image_height)}")
