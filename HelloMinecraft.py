# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x, y, z, block.TNT.id)
mc.setBlocks(x, y, z, x+10, y+30, z+10, block.TNT.id)
