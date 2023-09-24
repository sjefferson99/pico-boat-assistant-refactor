from lights.driver import Lights_Driver
from machine import Pin

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

def test_light_switched_on(mocker):
    mocked_Pin_on = mocker.patch('machine.Pin.on')
    lights_driver = Lights_Driver()
    lights_driver.light_on()
    mocked_Pin_on.assert_called_once()

def test_light_switched_of(mocker):
    mocked_Pin_off = mocker.patch('machine.Pin.off')
    lights_driver = Lights_Driver()
    lights_driver.light_off()
    mocked_Pin_off.assert_called_once()