#!/usr/bin/env python

import numpy as np
from PIL import Image

pix = np.asarray(Image.open("paisley.png"))

wide = np.concat([pix] * 4, axis=1)
big = np.concat([wide, wide])

# height_mm = 95.25
# width_mm = 304.8

# Image.fromarray(big).save("wide_paisley.png")
# print(big.shape)
in_ratio = big[:952, :3048, :]
Image.fromarray(in_ratio).save("wide_paisley.png")
