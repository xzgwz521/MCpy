import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import time

mc = minecraft.Minecraft.create("139.224.130.247", name="I_eat_potato")
pos = mc.player.getTilePos()
Blocks = {(255, 255, 255): 0,
          (255, 0, 0): 46}

print 'hello'

im = Image.open('hello3.png')
rgb_im = im.convert('RGB')
rows, columns = rgb_im.size
print rows, columns
for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))
        print rgb
        try:
            mc.setBlock(pos.x + r, pos.y, pos.z + c, Blocks[rgb])
        except:
            mc.setBlock(pos.x + r, pos.y, pos.z + c, block.TNT.id)
        time.sleep(0.05)


