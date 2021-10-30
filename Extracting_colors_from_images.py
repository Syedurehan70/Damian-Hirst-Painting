import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpeg', 30)

list_of_colors = []
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
for i in range(0, 30):
    color = colors[i]
    # rgb = color.rgb # e.g. (255, 151, 210)
    # in order to turn this into a format in which turtle can accept it
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_of_colors.append(new_color)

print(list_of_colors)
