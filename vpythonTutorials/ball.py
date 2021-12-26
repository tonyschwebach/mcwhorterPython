from vpython import *
from threading import Thread


class Ball:
    def __init__(self, color=color.red, radius=1):
        self.color = color
        self.radius = radius
        self.show()

    def show(self, startPosition=vector(0, 0, 0)):
        ball = sphere(color=self.color, radius=self.radius,
                      pos=startPosition)
        self.ball = ball
        return ball

    def changeColor(self):
        if (self.color != color.red):
            self.color = color.red
            self.ball.color = self.color
        else:
            self.color = color.green
            self.ball.color = self.color

    def move(self, room, changeColor=False, multiply=False):
        self.moveVector
        leftLimit = -room.roomLength/2+room.wallThickness/2
        rightLimit = room.roomLength/2-room.wallThickness/2
        topLimit = room.roomHeight/2 - room.wallThickness/2
        bottomLimit = -room.roomHeight/2 + room.wallThickness/2
        backLimit = -room.roomDepth/2 + room.wallThickness/2
        frontLimit = room.roomDepth/2 - room.wallThickness/2

        xPos = self.ball.pos.x
        yPos = self.ball.pos.y
        zPos = self.ball.pos.z
        if xPos < (leftLimit+self.radius) or xPos > (rightLimit-self.radius):
            self.moveVector.x *= -1
            if(changeColor):
                self.changeColor()
            if(multiply):
                self.multiply(room, self.moveVector)
        if yPos < (bottomLimit+self.radius) or yPos > (topLimit-self.radius):
            self.moveVector.y *= -1
            if(changeColor):
                self.changeColor()
            if(multiply):
                self.multiply(room, self.moveVector)
        if zPos < (backLimit+self.radius) or zPos > (frontLimit-self.radius):
            self.moveVector.z *= -1
            if(changeColor):
                self.changeColor()
            if(multiply):
                self.multiply(room, self.moveVector)
        newPos = self.ball.pos+self.moveVector
        self.ball.pos = newPos

    def multiply(self, room, moveVector, nBalls=2):
        # start at 1 due to division and multiplication
        for i in range(1, nBalls, 1):
            newBall = Ball(self.color, self.radius/nBalls)
            newBall.show(self.ball.pos)
            newBall.moveVector = moveVector/nBalls*i
            room.addBalls(newBall)
            # newBall.move(room, newVector, False, False)
            # newThread = Thread(target=newBall.move, args=(
            #     room, newVector, False, False))
            # newThread.daemon = True
            # newThread.start()
