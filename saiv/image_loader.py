# saiv/image_loader.py
from PIL import Image
import numpy as np
import colorsys

def load_image(image_path):
    img = Image.open(image_path).convert("RGB")
    return img

def resize_image(img, block_size):
    width, height = img.size
    width = (width // block_size) * block_size
    height = (height // block_size) * block_size
    img = img.resize((width, height))
    return img

def create_blocks(img, block_size, value_type="saturation"):
    pixels = np.array(img)
    img_width, img_height = img.size
    blocks = []

    for y in range(0, img_height, block_size):
        for x in range(0, img_width, block_size):
            block = pixels[y:y+block_size, x:x+block_size]
            avg_color = block.mean(axis=(0,1)).astype(int)
            r, g, b = avg_color / 255
            h, s, v = colorsys.rgb_to_hsv(r, g, b)

            if value_type == "saturation":
                value = s
            elif value_type == "hue":
                value = h
            elif value_type == "luminance":
                value = v
            else:
                raise ValueError("Invalid value_type")

            blocks.append({
                "pos": (x, y),
                "color": avg_color,
                "value": value,
                "block": block
            })

    return blocks, img_width, img_height
