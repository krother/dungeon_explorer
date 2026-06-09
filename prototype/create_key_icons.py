
import numpy as np
from PIL import Image, ImageDraw

COLORS = [
    ("red",    (200,  30,  30), (140,  20,  20)),
    ("blue",   ( 30,  80, 200), ( 20,  50, 140)),
    ("green",  ( 30, 180,  50), ( 20, 120,  35)),
    ("purple", (140,  30, 200), ( 90,  20, 140)),
    ("teal",   ( 30, 180, 170), ( 20, 120, 115)),
    ("yellow", (220, 200,  30), (150, 135,  20)),
]

for name, main, dark in COLORS:
    img = Image.open("floor.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    draw.ellipse([4, 9, 16, 21], outline=dark, fill=main, width=2)
    draw.ellipse([8, 13, 12, 17], outline=dark, fill=(0, 0, 0), width=1)
    draw.rectangle([13, 13, 27, 16], fill=main)
    draw.rectangle([21, 16, 23, 20], fill=main)
    draw.rectangle([25, 16, 27, 19], fill=main)

    img.save(f"key_{name}.png")

for name, main, dark in COLORS:
    arr = np.array(Image.open("closed_door.png").convert("RGBA"), dtype=float)

    # pixels where R - B > 15 are the wooden door panels (not the gray frame)
    door_mask = (arr[:, :, 0] - arr[:, :, 2]) > 15

    # luminance of each door pixel, remapped to 0.4–1.0 to brighten the result
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]) / 255.0
    lum = np.clip(lum * 0.6 + 0.4, 0.0, 1.0)

    for ch, value in enumerate(main):
        arr[:, :, ch] = np.where(door_mask, lum * value, arr[:, :, ch])

    Image.fromarray(arr.astype(np.uint8), "RGBA").save(f"door_{name}.png")
