from lights.driver import Lights_Driver
from lights.i2c_driver import Lights_I2C_Driver

class LightModule:
    def __init__(self) -> None:
        self.light_driver = Lights_Driver()
        self.i2c_driver = Lights_I2C_Driver()

    def configure_as_responder(self):
        self.i2c_driver.configure_responder()
