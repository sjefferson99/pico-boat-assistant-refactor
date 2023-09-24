from lights.driver import Lights_Driver
from machine import Pin

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

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