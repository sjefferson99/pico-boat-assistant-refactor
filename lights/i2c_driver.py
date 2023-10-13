import i2c_responder
from lights.driver import Lights_Driver

class Lights_I2C_Driver:
    """
    Create responder I2C instance that processes incoming I2C data and control light functions accordingly.
    1 byte data packet definition:
    First nibble:
    0x0 = Light on
    Second nibble:
    0x0-0xF = light IDs 0-15
    """
    def __init__(self) -> None:
        self.lights_driver = Lights_Driver()
        self.command_mask = 0xf0
        self.light_mask = 0x0f
        self.data_light_on = 0x00
        self.data_light_off = 0x10

    def process_I2C(self, data):
        if data & self.command_mask == self.data_light_on:
            self.lights_driver.light_on(data & self.light_mask)

        if data & self.command_mask == self.data_light_off:
            self.lights_driver.light_off(data & self.light_mask)