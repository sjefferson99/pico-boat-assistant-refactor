from machine import Pin

class Lights_Driver:
    def __init__(self) -> None:
        pass

    def light_on(self, id: int):
        light = Pin(id, Pin.OUT)
        light.on()
        return light
    
    def light_off(self, id: int):
        light = Pin(id, Pin.OUT)
        light.off()
        return light