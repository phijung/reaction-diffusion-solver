import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io

def save_gif(frames, filename, cmap="inferno", duration=100):
    """
    Create and save a gif.
    """

    images = []

    for frame in frames:
        fig, ax = plt.subplots()
        ax.imshow(frame, cmap=cmap)
        ax.axis("off")

        # Render figure to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        buf.seek(0)

        images.append(Image.open(buf))

    images[0].save(
        filename,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
