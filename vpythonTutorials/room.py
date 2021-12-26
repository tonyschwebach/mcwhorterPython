from vpython import *



class Room:
    def __init__(self, color, roomLength, roomHeight, roomDepth, wallThickness=0.1):
        self.color = color
        self.roomLength = roomLength
        self.roomHeight = roomHeight
        self.roomDepth = roomDepth
        self.wallThickness = wallThickness
        self.balls = []
        self.show()

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

    def addBalls(self, balls):
        if type(balls) == 'list':
            for ball in balls:
                self.balls.append(ball)
        # if type(balls) == "ball.Ball":
        else:
            self.balls.append(balls)

    def animate(self):
        while True:
            rate(25)
            for ball in self.balls:
                # print(index)
                # print(ball)
                ball.move(self,False,True)
