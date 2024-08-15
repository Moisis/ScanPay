from PIL import Image, ImageDraw, ImageFont
import os

# Define the font and size
font_path = 'ref/CREDC___.ttf'
font_size = 40
font = ImageFont.truetype(font_path, font_size)

# Create an image with a white background
image_width = 500
image_height = 50
image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Draw each digit
x_offset = 0
for digit in range(10):
    draw.text((x_offset, 0), str(digit), font=font, fill=(0, 0, 0))
    x_offset += 40  # Adjust spacing as needed

# Save the reference image
image.save('ref/ocr_a_reference.png')
