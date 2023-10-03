import pytest
from lights.driver import Lights_Driver
from machine import Pin, PWM

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

def test_all_light_pins_initialised():
    lights_driver = Lights_Driver()
    for light in lights_driver.lights:
        assert isinstance(light, Pin) == True

def test_all_light_pins_pwm_initialised():
    lights_driver = Lights_Driver()
    assert len(lights_driver.pwm_lights) > 0
    for light in lights_driver.pwm_lights:
        assert isinstance(light, PWM) == True

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

def test_init_sets_pwm_pin(mocker):
    lights_driver = Lights_Driver()
    light = lights_driver.light_pwm_init(Pin(0, Pin.OUT))

    assert isinstance(light, PWM)

def test_pwm_init_sets_pwm_frequency(mocker):
    mocked_PWM_freq = mocker.patch('machine.PWM.freq')
    lights_driver = Lights_Driver()
    lights_driver.light_pwm_init(Pin(0, Pin.OUT))
    mocked_PWM_freq.assert_any_call(1000)
    assert mocked_PWM_freq.call_count == 16

def test_set_light_to_half_brightness(mocker):
    mock_pwm_duty = mocker.patch("machine.PWM.duty_u16")
    
    lights_driver = Lights_Driver()
    light = lights_driver.light_pwm_init(Pin(0, Pin.OUT))
    lights_driver.set_brightness(light, 0.5)

    mock_pwm_duty.assert_called_once_with(32767)
