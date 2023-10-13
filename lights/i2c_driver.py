import i2c_responder
from lights.driver import Lights_Driver

class Lights_I2C_Driver:
    """
    Create responder I2C instance that processes incoming I2C data and control light functions accordingly.
    1 byte data packet definition:
    First nibble:
    0x0 = Set light off
    0x1 = Set light on
    0x2 = Set light brightness
    0xF = Reserved for extended command set
    Second nibble:
    0x0-0xF = light IDs 0-15
    """
    def __init__(self) -> None:
        self.lights_driver = Lights_Driver()
        self.command_mask = 0xf0
        self.light_mask = 0x0f
        self.data_light_off = 0x00
        self.data_light_on = 0x10
        self.data_light_brightness = 0x20

    def process_I2C(self, data: bytearray):
        if data[0] & self.command_mask == self.data_light_off:
            self.lights_driver.light_off(data[0] & self.light_mask)
        
        if data[0] & self.command_mask == self.data_light_on:
            self.lights_driver.light_on(data[0] & self.light_mask)
        
        if data[0] & self.command_mask == self.data_light_brightness:
            self.lights_driver.light_set_brightness(data[0] & self.light_mask, round(data[1] / 255, 2))