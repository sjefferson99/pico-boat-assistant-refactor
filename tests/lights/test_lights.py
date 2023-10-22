from lights import Light_Module
from lights.driver import Lights_Driver
from lights.i2c_driver import Lights_I2C_Driver
from i2c.i2c_responder import I2CResponder

def test_import_light_module():
    light_module = Light_Module()
    assert isinstance(light_module, Light_Module) == True

def test_light_module_has_light_driver():
    light_module = Light_Module()
    assert isinstance(light_module.light_driver, Lights_Driver) == True

def test_light_module_has_i2c_driver():
    light_module = Light_Module()
    assert isinstance(light_module.i2c_driver, Lights_I2C_Driver) == True

def test_i2c_driver_configures_as_responder():
    light_module = Light_Module()
    light_module.configure_as_responder()
    assert isinstance(light_module.i2c_driver.responder, I2CResponder)

def test_i2c_driver_configures_as_custom_responder():
    light_module = Light_Module()
    light_module.i2c_device_id=1
    light_module.sda_gpio=4
    light_module.scl_gpio=5
    light_module.responder_address=0x42
    light_module.configure_as_responder()
    assert isinstance(light_module.i2c_driver.responder, I2CResponder)
    assert light_module.i2c_driver.responder.i2c_device_id == 1
    assert light_module.i2c_driver.responder.sda_gpio == 4
    assert light_module.i2c_driver.responder.scl_gpio == 5
    assert light_module.i2c_driver.responder.responder_address == 0x42