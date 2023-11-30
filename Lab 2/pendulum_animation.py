#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2023  <asheragoodwin@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)
frame1 = [e,e,e,e,e,e,e,e,
         e,b,b,b,e,e,e,e,
         b,b,e,e,e,e,e,e,
         b,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         b,e,e,e,e,e,e,e,
         b,b,e,e,e,e,e,e] 
frame2 = [e,e,b,b,e,e,e,e,
         b,b,b,b,b,e,e,e,
         b,b,e,b,b,e,e,e,
         b,b,e,e,b,e,e,e,
         b,e,e,e,e,e,e,e,
         b,b,e,e,e,e,e,e,
         b,b,e,e,e,e,e,e,
         b,b,b,b,e,e,e,e] 
frame3 = [e,e,b,b,b,e,e,e,
         e,b,b,b,b,b,e,e,
         b,b,b,e,b,b,e,e,
         b,b,b,e,e,b,e,e,
         b,b,e,e,e,e,e,e,
         b,b,b,e,e,e,e,e,
         b,b,b,e,e,e,e,e,
         b,b,b,b,b,e,e,e] 
frame4 = [e,e,e,b,b,b,e,e,
         e,e,b,b,b,b,b,e,
         e,b,b,b,e,b,b,e,
         e,b,b,b,e,e,b,e,
         e,b,b,e,e,e,e,e,
         e,b,b,b,e,e,e,e,
         b,b,b,b,e,e,e,e,
         b,b,b,b,b,b,e,e] 
frame5 = [e,e,e,e,b,b,b,e,
         e,e,e,b,b,b,b,b,
         e,e,b,b,b,e,b,b,
         e,e,b,b,b,e,e,b,
         e,e,b,b,e,e,e,e,
         e,e,b,b,b,e,e,e,
         e,b,b,b,b,e,e,e,
         b,b,b,b,b,b,b,e] 
frame6 = [e,e,e,e,e,b,b,b,
         e,e,e,e,b,b,b,b,
         e,e,e,b,b,b,e,b,
         e,e,e,b,b,b,e,e,
         e,e,e,b,b,e,e,e,
         e,e,e,b,b,b,e,e,
         e,e,b,b,b,b,e,e,
         e,b,b,b,b,b,b,b] 
frame6 = [e,e,e,e,e,e,b,b,
         e,e,e,e,e,b,b,b,
         e,e,e,e,b,b,b,e,
         e,e,e,e,b,b,b,e,
         e,e,e,e,b,b,e,e,
         e,e,e,e,b,b,b,e,
         e,e,e,b,b,b,b,e,
         e,e,b,b,b,b,b,b] 
frame7 = [e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,b,b,b,
         e,e,e,e,e,b,b,b,
         e,e,e,e,e,b,b,e,
         e,e,e,e,e,b,b,b,
         e,e,e,e,b,b,b,b,
         e,e,e,b,b,b,b,b] 
frame8 = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,b,b,b,
         e,e,e,e,b,b,b,b] 
frame9 = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,b,b,
         e,e,e,e,e,b,b,b] 
frame10 = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,b,
         e,e,e,e,e,e,b,b] 
frame11 = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e] 



while True:
    sense.set_pixels(frame1)
    sleep(.1)
    sense.set_pixels(frame2)
    sleep(.1)
    sense.set_pixels(frame3)
    sleep(.1)
    sense.set_pixels(frame4)
    sleep(.1)
    sense.set_pixels(frame5)
    sleep(.1)
    sense.set_pixels(frame6)
    sleep(.1)
    sense.set_pixels(frame7)
    sleep(.1)
    sense.set_pixels(frame8)
    sleep(.1)
    sense.set_pixels(frame9)
    sleep(.1)
    sense.set_pixels(frame10)
    sleep(.1)
    sense.set_pixels(frame11)
    sleep(.25)