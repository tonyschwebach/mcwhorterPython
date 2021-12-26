from vpython import *
from time import *


class Room:
    def __init__(self, color, roomLength, roomHeight, roomDepth, wallThickness=0.1):
        self.color = color
        self.roomLength = roomLength
        self.roomHeight = roomHeight
        self.roomDepth = roomDepth
        self.wallThickness = wallThickness

    def show(self):
        ceiling = box(pos=vector(0, self.roomHeight/2, 0), color=self.color,
                      size=vector(self.roomLength, self.wallThickness, self.roomDepth))
        floor = box(pos=vector(0, -self.roomHeight/2, 0), color=self.color,
                    size=vector(self.roomLength, self.wallThickness, self.roomDepth))
        backWall = box(pos=vector(0, 0, -self.roomDepth/2), color=self.color,
                       size=vector(self.roomLength, self.roomHeight, self.wallThickness))
        leftWall = box(pos=vector(-self.roomLength/2, 0, 0), color=self.color,
                       size=vector(self.wallThickness, self.roomHeight, self.roomDepth))
        rightWall = box(pos=vector(self.roomLength/2, 0, 0), color=self.color,
                        size=vector(self.wallThickness, self.roomHeight, self.roomDepth))
        return [ceiling, floor, backWall, leftWall, rightWall]


class Ball:
    def __init__(self, color=color.red, radius=1):
        self.color = color
        self.radius = radius

    def show(self):
        ball = sphere(color=self.color, radius=self.radius)
        self.ball = ball
        return ball

    def move(self, speed=0.1, leftLimit=-10, rightLimit=10):
        xPos = 0
        # xPos = self.ball.pos
        # print(self.ball.pos)
        while True:
            rate(10)
            if xPos < (leftLimit+self.radius) or xPos > (rightLimit-self.radius):
                speed *= -1
            xPos += speed
            self.ball.pos = vector(xPos, 0, 0)


myRoom = Room(color.white, 10, 10, 10)
myRoom.show()
myMarble = Ball(color.green, 0.5)
myMarble.show()
myMarble.move(0.1,-5,5)

xPos = 0
while True:
    pass
# while True:
#     myMarble.move(1)
    # rate(10)
    # xPos += 10
    # myMarble.pos = vector(xPos, 0, 0)
