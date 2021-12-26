from room import Room
from ball import Ball
from vpython import vector,color




myRoom = Room(color.white, 10, 10, 10,1)
myMarble = Ball(color.green, 0.5)
myMarble.moveVector=vector(0.1,0.12,0.2)
myRoom.addBalls(myMarble)
myRoom.animate();
# myMarble.multiply(myRoom,movement)


while True:
    pass


