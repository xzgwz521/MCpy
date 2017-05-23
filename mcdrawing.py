# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()

mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos=mc.player.getTilePos()

RR = 20
#mcdrawing.drawLine(pos.x+3, pos.y, pos.z, pos.x+30, pos.y+30, pos.z+30,block.WOOL.id, 8)#画线
#mcdrawing.drawCircle(pos.x+20, pos.y+20, pos.z, RR, block.WOOL.id, 3)#画圆
#mcdrawing.drawSphere(pos.x+20, pos.y+20, pos.z+20, RR, block.WOOL.id, 5)#画球

points = []
points.append(minecraft.Vec3(pos.x+3, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x+13, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x+18, pos.y+10, pos.z))
points.append(minecraft.Vec3(pos.x+8, pos.y+10, pos.z))
mcdrawing.drawFace(points, True, block.WOOL.id, 3)

time.sleep(5)

points = []
points.append(minecraft.Vec3(pos.x+23, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x+28, pos.y+10, pos.z))
points.append(minecraft.Vec3(pos.x+33, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x+38, pos.y+10, pos.z))


mcdrawing.drawFace(points, True, block.WOOL.id, 3)

time.sleep(5)

