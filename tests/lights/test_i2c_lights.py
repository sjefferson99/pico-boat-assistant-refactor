from lights.i2c_driver import Lights_I2C_Driver
from i2c_responder import I2CResponder
from machine import mem32

I2C0_BASE = 0x40044000
IC_STATUS = 0x70
IC_STATUS__RFNE = 0x08

def test_import_lights_i2c():
    lights_i2c_driver = Lights_I2C_Driver()
    assert isinstance(lights_i2c_driver, Lights_I2C_Driver) == True

def test_turn_off_light_0_via_I2C_data(mocker):
    light_off_patch = mocker.patch('lights.driver.Lights_Driver.light_off')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x00]))
    light_off_patch.assert_called_once_with(0)

def test_turn_off_light_1_via_I2C_data(mocker):
    light_off_patch = mocker.patch('lights.driver.Lights_Driver.light_off')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x01]))
    light_off_patch.assert_called_once_with(1)

def test_turn_on_light_0_via_I2C_data(mocker):
    light_on_patch = mocker.patch('lights.driver.Lights_Driver.light_on')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x10]))
    light_on_patch.assert_called_once_with(0)

def test_turn_on_light_1_via_I2C_data(mocker):
    light_on_patch = mocker.patch('lights.driver.Lights_Driver.light_on')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x11]))
    light_on_patch.assert_called_once_with(1)

def test_set_brightness_for_light_0_via_I2C_data(mocker):
    set_brightness_patch = mocker.patch('lights.driver.Lights_Driver.light_set_brightness')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x20, 0x7f]))
    set_brightness_patch.assert_called_once_with(0, 0.5)

def test_set_different_brightness_for_light_0_via_I2C_data(mocker):
    set_brightness_patch = mocker.patch('lights.driver.Lights_Driver.light_set_brightness')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x20, 0x40]))
    set_brightness_patch.assert_called_once_with(0, 0.25)

def test_set_brightness_for_light_1_via_I2C_data(mocker):
    set_brightness_patch = mocker.patch('lights.driver.Lights_Driver.light_set_brightness')
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.process_I2C(bytearray([0x21, 0x7f]))
    set_brightness_patch.assert_called_once_with(1, 0.5)

def test_i2c_responder_configured():
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.configure_responder()
    assert isinstance(lights_i2c_driver.responder, I2CResponder) == True
    assert lights_i2c_driver.responder.i2c_device_id == 0
    assert lights_i2c_driver.responder.sda_gpio == 0
    assert lights_i2c_driver.responder.scl_gpio == 1
    assert lights_i2c_driver.responder.responder_address == 0x41

def test_i2c_responder_custom_configured():
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.configure_responder(i2c_device_id=0 , sda_gpio=16, scl_gpio=17, responder_address=0x41)
    assert isinstance(lights_i2c_driver.responder, I2CResponder) == True
    assert lights_i2c_driver.responder.i2c_device_id == 0
    assert lights_i2c_driver.responder.sda_gpio == 16
    assert lights_i2c_driver.responder.scl_gpio == 17
    assert lights_i2c_driver.responder.responder_address == 0x41

def test_i2c_responder_write_data_is_available():
    lights_i2c_driver = Lights_I2C_Driver()
    lights_i2c_driver.configure_responder(i2c_device_id=0 , sda_gpio=16, scl_gpio=17, responder_address=0x41)
    mem32[I2C0_BASE | IC_STATUS] = IC_STATUS__RFNE
    data_available = lights_i2c_driver.responder.write_data_is_available()
    assert data_available == True
