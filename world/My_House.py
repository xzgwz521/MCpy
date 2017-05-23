# -*- coding:utf-8 -*-

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import random
import math
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
#mc.player.setTilePos(20, 0, 20)

def ground(x=0, y=0, z=0, SIZE=20):
	#建造一个平地
	print('building ground')
	mc.setBlocks(x-SIZE/2, y, z-SIZE, x+SIZE/2, y, z+SIZE, block.STONE.id)
	mc.setBlocks(x-SIZE/2, y+1, z-SIZE*2, x+SIZE/2, y+SIZE, z+SIZE, block.AIR.id)
	print('building ground completed')

def cabin(x=0, y=0, z=0, SIZE = 16):
	print('start building')
	#设置随机数，决定羊毛的颜色,用于建造不同颜色的房子
	c = random.randint(0, 15)
	d = random.randint(0, 15)
	#建造房子主体，顶部为空
	mc.setBlocks(x-SIZE/2, y, z, x+SIZE/2, y+SIZE/2, z+SIZE, block.WOOL.id, d)
	mc.setBlocks(x-SIZE/2+1, y+1, z+1, x+SIZE/2-1, y+SIZE/2, z+SIZE-1, block.AIR.id)
	
	#建造屋顶
	#建造前屋顶
	points_front = []
	points_front.append(minecraft.Vec3(x-SIZE/2, y+SIZE/2, z))#前左点
	points_front.append(minecraft.Vec3(x, y+SIZE, z))#前中点
	points_front.append(minecraft.Vec3(x+SIZE/2, y+SIZE/2, z))#前右点
	mcdrawing.drawFace(points_front, True, block.WOOL.id, c)
	#建造后屋顶
	points_back = []
	points_back.append(minecraft.Vec3(x-SIZE/2, y+SIZE/2, z+SIZE))#后左点
	points_back.append(minecraft.Vec3(x, y+SIZE, z+SIZE))#后中点
	points_back.append(minecraft.Vec3(x+SIZE/2, y+SIZE/2, z+SIZE))#后右点
	mcdrawing.drawFace(points_back, True, block.WOOL.id, c)
	#建造左屋顶
	points_left = []
	points_left.append(minecraft.Vec3(x-SIZE/2, y+SIZE/2, z))#前左点
	points_left.append(minecraft.Vec3(x, y+SIZE, z))#前中点
	points_left.append(minecraft.Vec3(x, y+SIZE, z+SIZE))#后中点
	points_left.append(minecraft.Vec3(x-SIZE/2, y+SIZE/2, z+SIZE))#后左点
	mcdrawing.drawFace(points_left, True, block.WOOL.id, c)
	#建造右屋顶
	points_right = []
	points_right.append(minecraft.Vec3(x+SIZE/2, y+SIZE/2, z))#前右点
	points_right.append(minecraft.Vec3(x, y+SIZE, z))#前中点
	points_right.append(minecraft.Vec3(x, y+SIZE, z+SIZE))#后中点
	points_right.append(minecraft.Vec3(x+SIZE/2, y+SIZE/2, z+SIZE))#后右点
	mcdrawing.drawFace(points_right, True, block.WOOL.id, c)
	
	#建造门
	mc.setBlocks(x-1, y+1, z, x+1, y+4, z, block.AIR.id)
	#建造窗户
	mc.setBlocks(x-4, y+4, z, x-SIZE/2+2, y+SIZE/2-2, z, block.GLASS.id)
	mc.setBlocks(x+4, y+4, z, x+SIZE/2-2, y+SIZE/2-2, z, block.GLASS.id)
	
	print('cabin building completed')

def street():
	for i in range(0, 200 ,20):
		print(i)
		ground(x=i)
		time.sleep(1)
		cabin(x=i)
		time.sleep(3)

if __name__ == '__main__':
	street()	