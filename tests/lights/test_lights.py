from lights import LightModule
from lights.driver import Lights_Driver
from lights.i2c_driver import Lights_I2C_Driver

def test_import_light_module():
    light_module = LightModule()
    assert isinstance(light_module, LightModule) == True

def test_light_module_has_light_driver():
    light_module = LightModule()
    assert isinstance(light_module.light_driver, Lights_Driver) == True

def test_light_module_has_i2c_driver():
    light_module = LightModule()
    assert isinstance(light_module.i2c_driver, Lights_I2C_Driver) == True