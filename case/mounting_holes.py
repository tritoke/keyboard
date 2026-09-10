#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "sexpdata>=1.0.2",
# ]
# ///

from decimal import Decimal as D
import typing
from pathlib import Path

import sexpdata

script_dir = Path(__file__).parent
pcb_file = script_dir / "../pcb/keyboard.kicad_pcb"
pcb = sexpdata.loads(pcb_file.read_text())

mounting_holes = []
for item in pcb:
    if item[0] != sexpdata.Symbol("footprint"):
        continue

    if item[1] != "MountingHole:MountingHole_2.2mm_M2_Pad_Via":
        continue

    position = None
    for x in item:
        if x[0] == sexpdata.Symbol("at"):
            position = x[1:]
            break
    else:
        print("Failed to find position for mounting hole?")
        continue

    x, y = typing.cast(list[int], position)
    mounting_holes.append((x, y))

origin_x = D("47.625")
origin_y = D("76.200")
mounting_holes = sorted(mounting_holes)
for x, y in mounting_holes:
    print(f"{(x, y) = } => ({x - origin_x}, {y - origin_y})")
