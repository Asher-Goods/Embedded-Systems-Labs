from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    for event in sense.stick.get_events():

        if event.direction == "left" and event.action == "released":
            t = sense.get_temperature()
            t = round(t, 1)
            msg = "Temperature = {0}".format(t)
            sense.show_message(msg, scroll_speed=0.05)

        if event.direction == "right" and event.action == "released":
            with open("wave_animation.py") as f:
                exec(f.read())

        if event.direction == "up" and event.action == "released":
            with open("up.py") as f:
                exec(f.read())

        if event.direction == "down" and event.action == "released":
            with open("down.py") as f:
                exec(f.read())

        if event.direction == "middle" and event.action == "released":
            sense.clear()