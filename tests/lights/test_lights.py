import pytest
from lights.driver import Lights_Driver
from machine import Pin

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

def test_all_light_pins_initialised():
    lights_driver = Lights_Driver()
    lights_driver.init_all_pins()
    for light in lights_driver.lights:
        assert isinstance(light, Pin) == True

def test_light_switched_on(mocker):
    mocked_Pin_on = mocker.patch('machine.Pin.on')
    lights_driver = Lights_Driver()
    lights_driver.light_on(0)
    mocked_Pin_on.assert_called_once()

def test_light_switched_off(mocker):
    mocked_Pin_off = mocker.patch('machine.Pin.off')
    lights_driver = Lights_Driver()
    lights_driver.light_off(0)
    mocked_Pin_off.assert_called_once()

def test_specific_light_switched_on(mocker):
    def init_mock(self, id, mode):
        self.id = id
        self.mode = mode
    
    mocker.patch.object(Pin, "__init__", init_mock)
    
    lights_driver = Lights_Driver()
    light = lights_driver.light_on(0)

    assert isinstance(light, Pin)
    assert light.id == 0
    assert light.mode == Pin.OUT

def test_different_light_switched_on(mocker):
    def init_mock(self, id, mode):
        self.id = id
        self.mode = mode
    
    mocker.patch.object(Pin, "__init__", init_mock)
    
    lights_driver = Lights_Driver()
    light = lights_driver.light_on(1)

    assert isinstance(light, Pin)
    assert light.id == 1
    assert light.mode == Pin.OUT

def test_invalid_light_not_switched_on(mocker):    
    mocked_Pin_on = mocker.patch('machine.Pin.on')
    lights_driver = Lights_Driver()
    with pytest.raises(ValueError):
        lights_driver.light_on(17)
    mocked_Pin_on.assert_not_called()

def test_specific_light_switched_off(mocker):
    def init_mock(self, id, mode):
        self.id = id
        self.mode = mode
    
    mocker.patch.object(Pin, "__init__", init_mock)
    
    lights_driver = Lights_Driver()
    light = lights_driver.light_off(0)

    assert isinstance(light, Pin)
    assert light.id == 0
    assert light.mode == Pin.OUT

def test_different_light_switched_off(mocker):
    def init_mock(self, id, mode):
        self.id = id
        self.mode = mode
    
    mocker.patch.object(Pin, "__init__", init_mock)
    
    lights_driver = Lights_Driver()
    light = lights_driver.light_off(1)

    assert isinstance(light, Pin)
    assert light.id == 1
    assert light.mode == Pin.OUT

def test_invalid_light_not_switched_off(mocker):    
    mocked_Pin_off = mocker.patch('machine.Pin.off')
    lights_driver = Lights_Driver()
    with pytest.raises(ValueError):
        lights_driver.light_off(17)
    mocked_Pin_off.assert_not_called()

def test_set_pwn_frequency(mocker):
    mocked_PWM_freq = mocker.patch('machine.PWM.freq')
    lights_driver = Lights_Driver()
    lights_driver.light_pwm_init(0)
    mocked_PWM_freq.assert_called_once()

'''
light won't on/off if invalid gpio
light has been pwm init
'''