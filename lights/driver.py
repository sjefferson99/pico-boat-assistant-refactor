from machine import Pin

class Lights_Driver:
    def __init__(self) -> None:
        pass

    def light_on(self):
        light = Pin(0, Pin.OUT)
        light.on()