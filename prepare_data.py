import io

import numpy as np
from litdata import optimize
from PIL import Image

from config import load_config

# Load configuration
config = load_config()
output_dir = config.data.optimized_dir


# Store random images into the data chunks
def random_images(index):
    """Generates a random image and saves it as JPEG bytes."""
    # Create a random image using PIL
    pil_image = Image.fromarray(np.random.randint(0, 256, (32, 32, 3), np.uint8))

    # Save the image to an in-memory buffer as JPEG
    with io.BytesIO() as buffer:
        pil_image.save(buffer, format="JPEG")
        jpeg_bytes = buffer.getvalue()
    
    jpeg_image = Image.open(io.BytesIO(jpeg_bytes))

    data = {
        "index": index,  # int data type
        "image": jpeg_image,  # JPEG image
        "class": np.random.randint(10),  # class
    }
    return data


if __name__ == "__main__":
    optimize(
        fn=random_images,  # The function applied over each input.
        inputs=list(range(1000)),  # Provide any inputs. The fn is applied on each item.
        output_dir=output_dir,  # The directory where the optimized data are stored.
        num_workers=4,  # The number of workers. The inputs are distributed among them.
        chunk_bytes="64MB",  # The maximum number of bytes to write into a data chunk.
    )
