import pytest
from lights.driver import Lights_Driver
from machine import Pin, PWM

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

def test_all_lights_initialised(mocker):
    mocked_light_pwm_init = mocker.patch("lights.driver.Lights_Driver.light_pwm_init")
    lights_driver = Lights_Driver()
    calls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert len(mocked_light_pwm_init.mock_calls) == len(calls)

def test_all_light_pins_pwm_initialised():
    lights_driver = Lights_Driver()
    assert len(lights_driver.lights) > 0
    for light in lights_driver.lights:
        assert isinstance(light, PWM) == True

def test_light_switched_on(mocker):
    mocked_pwm_on = mocker.patch('machine.PWM.duty_u16')
    lights_driver = Lights_Driver()
    lights_driver.light_on(0)
    mocked_pwm_on.assert_called_once_with(65535)

def test_light_switched_off(mocker):
    mocked_pwm_on = mocker.patch('machine.PWM.duty_u16')
    lights_driver = Lights_Driver()
    lights_driver.light_off(0)
    mocked_pwm_on.assert_called_once_with(0)

def test_specific_light_switched_on(mocker):
    mocked_set_brightness = mocker.patch("lights.driver.Lights_Driver.set_brightness")
    lights_driver = Lights_Driver()
    lights_driver.light_on(0)
    mocked_set_brightness.assert_called_once_with(lights_driver.lights[0], 1)

def test_different_light_switched_on(mocker):
    mocked_set_brightness = mocker.patch("lights.driver.Lights_Driver.set_brightness")
    lights_driver = Lights_Driver()
    lights_driver.light_on(4)
    mocked_set_brightness.assert_called_once_with(lights_driver.lights[4], 1)

def test_invalid_light_not_switched_on(mocker):    
    mocked_Pin_on = mocker.patch('machine.Pin.on')
    lights_driver = Lights_Driver()
    with pytest.raises(ValueError):
        lights_driver.light_on(17)
    mocked_Pin_on.assert_not_called()

def test_specific_light_switched_off(mocker):
    mocked_set_brightness = mocker.patch("lights.driver.Lights_Driver.set_brightness")
    lights_driver = Lights_Driver()
    lights_driver.light_off(0)
    mocked_set_brightness.assert_called_once_with(lights_driver.lights[0], 0)

def test_different_light_switched_off(mocker):
    mocked_set_brightness = mocker.patch("lights.driver.Lights_Driver.set_brightness")
    lights_driver = Lights_Driver()
    lights_driver.light_off(5)
    mocked_set_brightness.assert_called_once_with(lights_driver.lights[5], 0)

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
    mocked_PWM_freq.assert_any_call(1000)
    assert mocked_PWM_freq.call_count == 16

def test_set_light_to_half_brightness(mocker):
    mock_pwm_duty = mocker.patch("machine.PWM.duty_u16")
    
    lights_driver = Lights_Driver()
    light = lights_driver.lights[0]
    lights_driver.set_brightness(light, 0.5)

    mock_pwm_duty.assert_called_once_with(32767)

def test_cant_set_brightness_less_than_0(mocker):
    mocked_pwm_on = mocker.patch('machine.PWM.duty_u16')
    lights_driver = Lights_Driver()
    light0 = lights_driver.lights[0]
    with pytest.raises(ValueError):
        lights_driver.set_brightness(light0, -0.1)
    mocked_pwm_on.assert_not_called()

def test_cant_set_brightness_greater_than_1(mocker):
    mocked_pwm_on = mocker.patch('machine.PWM.duty_u16')
    lights_driver = Lights_Driver()
    light0 = lights_driver.lights[0]
    with pytest.raises(ValueError):
        lights_driver.set_brightness(light0, 1.1)
    mocked_pwm_on.assert_not_called()

def test_specific_light_brightness_set_by_id(mocker):
    mocked_set_brightness = mocker.patch("lights.driver.Lights_Driver.set_brightness")
    lights_driver = Lights_Driver()
    lights_driver.light_set_brightness(0, 0.5)
    mocked_set_brightness.assert_called_once_with(lights_driver.lights[0], 0.5)

def test_set_all_lights_off(mocker):
    mocked_light_off = mocker.patch("lights.driver.Lights_Driver.light_off")
    lights_driver = Lights_Driver()
    lights_driver.all_lights_off()
    calls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for call in calls:
        mocked_light_off.assert_any_call(call)

def test_set_all_lights_on(mocker):
    mocked_light_on = mocker.patch("lights.driver.Lights_Driver.light_on")
    lights_driver = Lights_Driver()
    lights_driver.all_lights_on()
    calls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for call in calls:
        mocked_light_on.assert_any_call(call)