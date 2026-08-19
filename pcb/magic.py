#!/usr/bin/env python

import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation, binary_erosion


def pix_and(*args: np.ndarray) -> np.ndarray:
    pix = args[0]
    for pix_ in args[1:]:
        pix *= pix_
    return pix


def pix_or(*args: np.ndarray) -> np.ndarray:
    pix = args[0]
    for pix_ in args[1:]:
        pix += pix_
    return pix


def near(img: np.ndarray, pix: list[int], margin: int) -> np.ndarray:
    a = []
    for i, v in enumerate(pix):
        a.append(np.abs(img[:, :, i] - v) <= margin)

    return pix_and(*a)


def near2(img: np.ndarray, r: set[int], g: set[int], b: set[int]) -> np.ndarray:
    rs = []
    gs = []
    bs = []

    for rp in r:
        rs.append(img[:, :, 0] == rp)
    for gp in g:
        gs.append(img[:, :, 1] == gp)
    for bp in b:
        bs.append(img[:, :, 2] == bp)

    return pix_and(pix_or(*rs), pix_or(*gs), pix_or(*bs))


pix = np.asarray(Image.open("pfp.png"))

noalpha = pix[:, :, :3]
r = pix[:, :, 0]
g = pix[:, :, 1]
b = pix[:, :, 2]

edges = [
    near(noalpha, [0, 10, 7], 10),
    near(noalpha, [54, 43, 26], 10),
    near(noalpha, [20, 23, 22], 2),
    near(noalpha, [20, 23, 22], 2),
    near(noalpha, [19, 136, 212], 50),
    # near(noalpha, [253, 181, 57], 1),
    near2(
        noalpha,
        set(range(18, 23)),
        set(range(130, 147)),
        set(range(202, 213)),
    ),
    pix_and(r < 30, g < 30, b < 30),
    near2(
        noalpha,
        set(range(35, 70)),
        set(range(25, 55)),
        set(range(15, 35)),
    ),
    near2(
        noalpha,
        {37, 38},
        {30},
        {18},
    ),
    near2(
        noalpha,
        set(range(35, 60)),
        set(range(135, 190)),
        set(range(110, 160)),
    ),
    near2(
        noalpha,
        set(range(8, 32)),
        set(range(12, 50)),
        set(range(8, 40)),
    ),
    near2(
        noalpha,
        set(range(40, 55)),
        set(range(40, 55)),
        set(range(40, 55)),
    ),
]

edge = pix_or(*edges)

# fmt: off
kernel = [
    [False, True, False],
    [True,  True, True],
    [False, True, False],
]
# fmt: on
img = binary_dilation(edge, kernel)
img = binary_dilation(img, kernel)
img = binary_dilation(img, kernel)
img = binary_dilation(img, kernel)
img = binary_erosion(img, kernel)
img = binary_erosion(img, kernel)
img = binary_erosion(img, kernel)
img = binary_erosion(img, kernel)

# # fmt: off
# kernel = [
#     [False, False, True, False, False],
#     [False, True,  True, True,  False],
#     [True,  True,  True, True,  True],
#     [False, True,  True, True,  False],
#     [False, False, True, False, False],
# ]
# # fmt: on
# img = binary_dilation(edge, kernel)
# img = binary_erosion(img, kernel)
out = Image.fromarray(img * np.uint8(255))
out.save("out.png")

out_small = out.resize((112, 132))
out_small.save("out_small.png")
