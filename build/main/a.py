from PIL import Image
from PIL import ImageDraw
import math

sz = (1080, 720)
wt = (255, 255, 255)
blk = (0, 0, 0)
points = ((100, 200), (300, 400), (500, 150), (300, 600), (100, 200))
fence = 300

if __name__ == "__main__":
    im = Image.new("RGB", sz, wt)
    # im.show()
    m = ImageDraw.Draw(im)
    m.line(points, blk)
    im.show()
    weight = sz[0]
    height = sz[1]
    for j in range(height):
        lst = list()
        for i in range(weight):
            if im.getpixel((i, j)) == blk and (i, j) not in points:
                lst.append(i)
        # print(lst)
        for item in lst:
            if item < fence:
                for i in range(item, fence):
                    if im.getpixel((i, j)) == blk:
                        im.putpixel((i, j), wt)
                    else:
                        im.putpixel((i, j), blk)

            elif item > fence:
                for i in range(fence, item):
                    if im.getpixel((i, j)) == blk:
                        im.putpixel((i, j), wt)
                    else:
                        im.putpixel((i, j), blk)

    im.show()
