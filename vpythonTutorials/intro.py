from numpy import right_shift
from vpython import *

origin = sphere(color=color.red, radius=0.1)
roomLength = 3  # x
roomHeight =7  # y
roomWidth = 16  # z
wallThickness = 0.1
ceiling = box(pos=vector(0, roomHeight/2, 0), color=color.orange,
              length=roomLength, height=wallThickness, width=roomWidth)
floor = box(pos=vector(0, -roomHeight/2, 0), color=color.yellow,
            length=roomLength, height=wallThickness, width=roomWidth)
backWall = box(pos=vector(0, 0, -roomWidth/2), color=color.white,
               length=roomLength, height=roomHeight, width=wallThickness)
leftWall = box(pos=vector(-roomLength/2, 0, 0), color=color.green,
               length=wallThickness, height=roomHeight, width=roomWidth)
rightWall = box(pos=vector(roomLength/2, 0, 0), color=color.green,
                length=wallThickness, height=roomHeight, width=roomWidth)


# final = box(pos=vector(0,0,0),color=color.white,length=roomLength,height=roomHeight,width=roomWidth)


while True:
    pass
