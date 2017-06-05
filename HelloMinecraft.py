# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create("139.224.130.247", name="I_eat_potato")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# mc.setBlock(x+1, y, z, block.TNT.id)  # 放置一个TNT
#mc.setBlocks(x, y, z, x+10, y+30, z+10, block.TNT.id)

# mc.setBlocks(x+8, y+6, z, x+8, y, z, block.TNT.id)

mc.setBlock(x, y, z, block.TNT.id)


for i in range(0, 10):
    mc.setBlock(x+i, y+i, z+i, block.TNT.id)



