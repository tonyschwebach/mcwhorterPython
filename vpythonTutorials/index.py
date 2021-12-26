from room import *
from ball import *
from vpython import vector




myRoom = Room(color.white, 10, 10, 10,1)
myRoom.show()
myMarble = Ball(color.green, 0.5)
myMarble.show()
movement=vector(0.02,0.06,0.03)
myMarble.move(myRoom,movement,False,True)
# myMarble.multiply(myRoom,movement)


while True:
    pass


