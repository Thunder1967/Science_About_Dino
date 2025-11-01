#pyinstaller auto_modify_photo\auto_modify_photo.py --onefile
# place_with_scale.py
# 需求: pillow
from PIL import Image

# 格式: (x_left, y_bottom, height, width)
PLACES = [(76, 96, 90, 90)]\
+[(1678+x*88,96,94,88) for x in range(6)]\
+[(2206+x*118,96,60,118) for x in range(2)]
# [
#     (40, 49, 45, 45),
# ]+[(845+x*45,49,47,45) for x in range(6)]

def load_rgba(path):
    return Image.open(path).convert("RGBA")

def resize_sprite(img, h, w):
    if h is None and w is None:
        return img
    if h is None:
        r = w / img.width
        h = int(img.height * r)
    elif w is None:
        r = h / img.height
        w = int(img.width * r)
    return img.resize((max(1, int(w)), max(1, int(h))), Image.BICUBIC)
def clear_rect(img, x_left, y_bottom, h, w):
    # 把矩形區域 alpha 清為 0
    x0 = int(round(x_left))
    y0 = int(round(y_bottom - h))  # 轉成左上 y
    x1 = x0 + int(round(w))
    y1 = y0 + int(round(h))
    # 邊界裁切
    x0 = max(0, x0); y0 = max(0, y0)
    x1 = min(img.width, x1); y1 = min(img.height, y1)
    if x0 >= x1 or y0 >= y1:
        return
    region = img.crop((x0, y0, x1, y1))
    r, g, b, a = region.split()
    a = Image.new("L", (x1 - x0, y1 - y0), 0)
    region.putalpha(a)
    img.paste(region, (x0, y0, x1, y1))

def paste_bottom_left(base, sprite, x_left, y_bottom):
    sw, sh = sprite.size
    x = int(round(x_left))
    y = int(round(y_bottom - sh))
    base.alpha_composite(sprite, (x, y))

def main():
    base_path = "original_dino_big.png"
    char_path = input("input the role file name : ")
    out_path = "output.png"

    base = load_rgba(base_path)
    sprite_raw = load_rgba(char_path)

    out = base.copy()
    for (x, y, h, w) in PLACES:
        clear_rect(out, x, y, h, w)
        sp = resize_sprite(sprite_raw, h, w)
        paste_bottom_left(out, sp, x, y)

    out.save(out_path)
    print("已輸出", out_path)

if __name__ == "__main__":
    main()
