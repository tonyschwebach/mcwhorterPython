from vpython import *
from threading import Thread


class Ball:
    def __init__(self, color=color.red, radius=1):
        self.color = color
        self.radius = radius

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

    def move(self, room, moveVector=vector(0.1, 0, 0), changeColor=False, multiply=False):
        leftLimit = -room.roomLength/2+room.wallThickness/2
        rightLimit = room.roomLength/2-room.wallThickness/2
        topLimit = room.roomHeight/2 - room.wallThickness/2
        bottomLimit = -room.roomHeight/2 + room.wallThickness/2
        backLimit = -room.roomDepth/2 + room.wallThickness/2
        frontLimit = room.roomDepth/2 - room.wallThickness/2
        while True:
            xPos = self.ball.pos.x
            yPos = self.ball.pos.y
            zPos = self.ball.pos.z
            rate(100)
            if xPos < (leftLimit+self.radius) or xPos > (rightLimit-self.radius):
                moveVector.x *= -1
                if(changeColor):
                    self.changeColor()
                if(multiply):
                    self.ball.visible = False
                    self.multiply(room, moveVector)
            if yPos < (bottomLimit+self.radius) or yPos > (topLimit-self.radius):
                moveVector.y *= -1
                if(changeColor):
                    self.changeColor()
            if zPos < (backLimit+self.radius) or zPos > (frontLimit-self.radius):
                moveVector.z *= -1
                if(changeColor):
                    self.changeColor()
            newPos = self.ball.pos+moveVector
            self.ball.pos = newPos

    def multiply(self, room, moveVector, nBalls=2):
        for i in range(1, nBalls, 1):
            newBall = Ball(self.color, self.radius/nBalls)
            newBall.show(self.ball.pos)
            newVector = moveVector/nBalls*i
            # newBall.move(room, newVector, False, False)
            newThread = Thread(target=newBall.move, args=(
                room, newVector, False, False))
            newThread.daemon = True
            newThread.start()
