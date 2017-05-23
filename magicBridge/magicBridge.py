# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time

#mc = minecraft.Minecraft.create("118.89.102.156")
mc = minecraft.Minecraft.create()

bridge = []


def buildBridge():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    b = mc.getBlock(x, y-1, z)
    if b == block.WATER_FLOWING.id or b == block.AIR.id or  b == block.WATER.id:
        mc.setBlock(x, y-1, z, block.GLASS.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.2)

while True:
    time.sleep(0)
    buildBridge()
