#!/usr/bin/env python3

import yaml
import sys

mapping_path = sys.argv[1]
with open(mapping_path, "r") as f:
    t: dict[str, str] = yaml.load(f, yaml.Loader)

palette = [
    ["header", [t["red_glowing"], "bold"], None],
    ["footer", [t["red_glowing"], "bold"], None],
    ["line header", [t["background"], "bold"], [t["orange_blaze"]]],
    ["alt header", [t["text"]], None],
    ["list", [t["background"], "bold"], [t["orange_blaze"]]],
    ["edit", [t["orange_blaze"]], None],
]

for item in palette:
    key = item[0]
    fg, bg = "default", "default"
    fgt, bgt = item[1], item[2]
    if fgt is not None:
        if len(fgt) > 1:
            fg = ",".join(fgt)
        else:
            fg = fgt[0]
    if bgt is not None:
        if len(bgt) > 1:
            bg = ",".join(bgt)
        else:
            bg = bgt[0]
    print(f"{key} = '', '', '', '{fg}', '{bg}'")
