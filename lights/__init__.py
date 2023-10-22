from lights.driver import Lights_Driver
from lights.i2c_driver import Lights_I2C_Driver

class Light_Module:
    def __init__(self) -> None:
        self.light_driver = Lights_Driver()
        self.i2c_driver = Lights_I2C_Driver()
        self.i2c_device_id=0
        self.sda_gpio=16
        self.scl_gpio=17
        self.responder_address=0x41

    def configure_as_responder(self) -> None:
        self.i2c_driver.configure_responder(self.i2c_device_id, self.sda_gpio, self.scl_gpio, self.responder_address)
