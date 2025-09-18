# saiv/visualizer.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Visualizer:
    def __init__(self, blocks, img_width, img_height, block_size):
        self.blocks = blocks
        self.img_width = img_width
        self.img_height = img_height
        self.block_size = block_size

        self.canvas = np.zeros((img_height, img_width, 3), dtype=np.uint8)
        self.frames = []

    def capture_frame(self, arr=None):
        arr = arr or self.blocks
        for idx, b in enumerate(arr):
            x = (idx % (self.img_width // self.block_size)) * self.block_size
            y = (idx // (self.img_width // self.block_size)) * self.block_size
            self.canvas[y:y+self.block_size, x:x+self.block_size] = b['block']
        self.frames.append(self.canvas.copy())

    def animate(self, interval=50):
        fig, ax = plt.subplots()
        im = ax.imshow(self.canvas)
        ax.axis('off')

        def update(frame):
            im.set_data(frame)
            return [im]

        import matplotlib.animation as animation
        ani = animation.FuncAnimation(fig, update, frames=self.frames, interval=interval, blit=True)
        plt.show()

    def save_final_image(self, filename):
        final_canvas = np.zeros((self.img_height, self.img_width, 3), dtype=np.uint8)
        for idx, b in enumerate(self.blocks):
            x = (idx % (self.img_width // self.block_size)) * self.block_size
            y = (idx // (self.img_width // self.block_size)) * self.block_size
            final_canvas[y:y+self.block_size, x:x+self.block_size] = b['block']
        img = Image.fromarray(final_canvas)
        img.save(filename)
        print(f"Sorted image saved as {filename}")
