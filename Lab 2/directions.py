import random
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
 acceleration = sense.get_accelerometer_raw()
 x = acceleration['x']
 y = acceleration['y']
 z = acceleration['z']

 x=round(x, 1)
 y=round(y, 1)
 z=round(z, 1)


 if x<-.1 and y>=0 and z>=0 :
    for col in range(7,-1,-1):
       color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
       for row in range (8):
          sense.set_pixel(col,row,color)
       sleep(.075)
       sense.clear()

 if x>.1 and y>=0 and z>=0 :
   for col in range(0,8,1):
       color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
       for row in range (8):
          sense.set_pixel(col,row,color)
       sleep(.075)
       sense.clear()

 if x>=0 and y<-.1 and z>=0 :
   for row in range(7,-1,-1):
       color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
       for col in range (8):
          sense.set_pixel(col,row,color)
       sleep(.075)
       sense.clear()

 if x>=0 and y>.1 and z>=0 :
    for row in range(8):
       color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
       for col in range (8):
          sense.set_pixel(col,row,color)
       sleep(.075)
       sense.clear()

 if x>=0 and y>=0 and z>=.9 :
    message = "UP"
    sense.show_message(message,0.05,text_colour=(255,0,0),back_colour=(0,0,0))

 if x>=0 and y>=0 and z<=-.9 :
    print("Down")