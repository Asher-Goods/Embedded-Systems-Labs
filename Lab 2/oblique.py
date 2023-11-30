
from sense_hat import SenseHat
import time
import random
from time import sleep
sense = SenseHat()

colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255), (128,0,0), (128,128,0)]


 
def display_line(start_x,start_y,color):
    x,y = start_x, start_y
    while x>= 0 and y>= 0:
      sense.set_pixel(x,y,color)
      time.sleep(.2)
      x -=1
      y -=1
      sense.clear()

def display_diagonal():
   row = 0
   for row in range(9):
      color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
      for col in range(row):
         sense.set_pixel(col,row-col-1,color)
      time.sleep(.2)
      sense.clear()
   
   q = 0
   for x in range(0,7,1):
      col = q +1
      color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
      for row in range(7,q,-1):
            sense.set_pixel(col,row,color)
            col+=1
      time.sleep(.2)
      sense.clear()
      q+=1
   

display_diagonal()
 