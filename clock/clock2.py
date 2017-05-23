import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
from datetime import datetime

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


def put_number(x=0, y=0, z=0, number=0):
    zero = [(1, 1, 1), (1, 0, 1), (1, 0, 1), (1, 0, 1), (1, 1, 1)]
    one = [(1, 1, 1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (1, 1, 0)]
    two = [(1, 1, 1), (1, 0, 0), (1, 1, 1), (0, 0, 1), (1, 1, 1)]
    three = [(1, 1, 1), (0, 0, 1), (1, 1, 1), (0, 0, 1), (1, 1, 1)]
    four = [(0, 0, 1), (0, 0, 1), (1, 1, 1), (1, 0, 1), (1, 0, 1)]
    five = [(1, 1, 1), (0, 0, 1), (1, 1, 1), (1, 0, 0), (1, 1, 1)]
    six = [(1, 1, 1), (1, 0, 1), (1, 1, 1), (1, 0, 0), (1, 1, 1)]
    seven = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (1, 0, 1), (1, 1, 1)]
    eight = [(1, 1, 1), (1, 0, 1), (1, 1, 1), (1, 0, 1), (1, 1, 1)]
    nine = [(1, 1, 1), (0, 0, 1), (1, 1, 1), (1, 0, 1), (1, 1, 1)]

    list_number = [zero, one, two, three, four, five, six, seven, eight, nine]
    a = random.randint(0, 15)
    for Tuple in list_number[number]:
        xx = x
        for cell in Tuple:
            if cell == 1:
                b = block.REDSTONE_BLOCK.id
                mc.setBlock(x, y, z, b, 1)
            else:
                b = block.AIR.id
                mc.setBlock(x, y, z, b)
            x = x+1
        y = y+1
        x = xx

mc.setBlocks(pos.x, pos.y, pos.z-4, pos.x+26, pos.y+4, pos.z-4, block.REDSTONE_LAMP.id)

while True:
    today = datetime.now()
    hours = today.hour
    minutes = today.minute
    seconds = today.second
    print hours, minutes, seconds

    put_number(pos.x, pos.y, pos.z-5, hours//10)
    put_number(pos.x+4, pos.y, pos.z-5, hours % 10)
    mc.setBlock(pos.x+8, pos.y+1, pos.z-5, block.REDSTONE_BLOCK.id)
    mc.setBlock(pos.x+8, pos.y+3, pos.z-5, block.REDSTONE_BLOCK.id)
    put_number(pos.x+10, pos.y, pos.z-5, minutes//10)
    put_number(pos.x+14, pos.y, pos.z-5, minutes % 10)
    mc.setBlock(pos.x+18, pos.y+1, pos.z-5, block.REDSTONE_BLOCK.id)
    mc.setBlock(pos.x+18, pos.y+3, pos.z-5, block.REDSTONE_BLOCK.id)
    put_number(pos.x+20, pos.y, pos.z-5, seconds//10)
    put_number(pos.x+24, pos.y, pos.z-5, seconds % 10)

    time.sleep(1)
