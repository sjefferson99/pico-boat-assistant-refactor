import i2c_responder
from lights.driver import Lights_Driver

class Lights_I2C_Driver:
    def __init__(self) -> None:
        self.lights_driver = Lights_Driver()

    def process_I2C(self, data):
        self.lights_driver.light_on(0)