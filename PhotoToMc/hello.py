import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
Blocks = {(255, 255, 255): 0,
          (237, 28, 36): 46}

# print 'hello'

im = Image.open('twb.png')
rgb_im = im.convert('RGB')
rows, columns = rgb_im.size
print rows, columns
for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))
        if rgb == Blocks[(237, 28, 36)]:
            mc.setBlock(pos.x + r, pos.y, pos.z + c, Blocks[rgb])
            time.sleep(0.02)