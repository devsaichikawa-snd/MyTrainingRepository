import numpy as np
from PIL import Image


# l = np.array([[0, 128, 255], [0, 128, 255], [0, 128, 255]])
row_data = np.arange(256)
im_data = np.tile(row_data, (255, 1))
# print(im_data)

# print(row_data)
im = Image.fromarray(np.uint8(im_data), "L")
im.show()
