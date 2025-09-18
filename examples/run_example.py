# examples/run_example.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from saiv.image_loader import load_image, resize_image, create_blocks
from saiv.sorting import merge_sort, quick_sort, bubble_sort
from saiv.visualizer import Visualizer

image_path = "images/example.png"
block_size = 50
value_type = "saturation"        # "saturation", "hue", or "luminance"
algorithm_to_use = "quick"       # "merge", "quick", or "bubble"

# load and resize image
img = load_image(image_path)
img = resize_image(img, block_size)

# create blocks
blocks, img_width, img_height = create_blocks(img, block_size, value_type=value_type)

# initialize visualizer
viz = Visualizer(blocks, img_width, img_height, block_size)

# choose sorting algorithm
sorting_algorithms = {
    "merge": merge_sort,
    "quick": quick_sort,
    "bubble": bubble_sort
}

sort_func = sorting_algorithms.get(algorithm_to_use)
if not sort_func:
    raise ValueError(f"Invalid algorithm: {algorithm_to_use}")

# run sorting with frame capturing
sort_func(blocks, capture_frame=viz.capture_frame)

# animate sorting
viz.animate(interval=50)

# save final sorted image
output_filename = f"output/{algorithm_to_use}_sorted_by_{value_type}.png"
viz.save_final_image(output_filename)
