from PIL import Image

image_original = Image.open("images/beach.jpg")

cactus_image = Image.open("images/cactus.jpg")
cactus_pixels = cactus_image.load()

image_combined = Image.new("RGB", image_original.size)

# image_original.show()

width, height = image_original.size

print(width, height)

pixels_original = image_original.load()

# r, g, b = pixels_original[600, 200]

# Don't forget to use parentheses around your (r, g, b)
# pixels_original[100, 200] = (r, g, b)
# pixels_original[200, 200] = (r, g, b)
#
# pixels_original[200, 300] = (255, 0, 0)
# pixels_original[100, 100] = (255, 0, 0)
# pixels_original[150, 50] = (255, 0, 0)
# pixels_original[100, 300] = (255, 0, 0)
# pixels_original[250, 300] = (255, 0, 0)

print(cactus_pixels[100, 200])
# cactus_pixels[210, 200] = (255, 0, 0)
print(cactus_pixels[210, 200])

green = 244

for x in range(width):
    for y in range(height):
        r, g, b = cactus_pixels[x, y]
        new_green = g + 30
        new_red = r - 30
        cactus_pixels[x, y] = (new_red, new_green, b)

# Adding a layer of green to the image
for x in range(width):
    for y in range(height):
        r, g, b = pixels_original[x, y]
        new_green = g + 50
        # new_red = r - 30
        pixels_original[x, y] = (r, new_green, b)

# print(cactus_pixels[210, 200])
# print(cactus_pixels[100, 200])

# for x in range(width):
#     for y in range(height):
#         (r, g, b) = pixels_original[x, y]
#
#         # new_red = r + 50
#         # pixels_original[x, y] = (r, g, b)
#         if cactus_pixels[x, y] == (83, 255, 26) or cactus_pixels[x, y] == (76, 255, 24) or cactus_pixels[x, y] == (46, 255, 24):
#             cactus_pixels[x, y] = (r, g, b)
#         # if pixels_original[x, y] == (76, 244, 24):
#         #     pixels_original[x, y] = (0, 0, 255)

image_original.show()
# cactus_pixels[width-1, 10] = (255, 0, 0)
# print(cactus_pixels[(width/2)+35, height/2])
# cactus_pixels[(width/2)+35, height/2] = (255, 0, 0)
# cactus_image.show()
image_original.save("the_file_goes_here.jpg")


# print(r, g, b)