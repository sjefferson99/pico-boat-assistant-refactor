from lights.i2c_driver import Lights_I2C_Driver

def test_import_lights_i2c():
    lights_i2c_driver = Lights_I2C_Driver()
    assert isinstance(lights_i2c_driver, Lights_I2C_Driver) == True